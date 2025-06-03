import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder
from datetime import datetime

# Load data
df = pd.read_csv("assets/game_log.csv")

# Add days_since_start
df['date'] = pd.to_datetime(df['date'])
start_date = df['date'].min()
df['days_since_start'] = (df['date'] - start_date).dt.days

# Fill missing pitcherHand just in case
df['pitcherHand'] = df['pitcherHand'].fillna('R')

# --- Add opponent_recent_K_percent ---
df.sort_values(by='date', inplace=True)
df['K_percent'] = df['strikeouts'] / df['battersFaced']

df['opponent_recent_K_percent'] = (
    df.groupby('opponent')['K_percent']
    .transform(lambda x: x.shift().rolling(5, min_periods=1).mean())
)

# --- Add opponent_recent_K_percent_vs_hand ---
df['opponent_recent_K_percent_vs_hand'] = (
    df.groupby(['opponent', 'pitcherHand'])['K_percent']
    .transform(lambda x: x.shift().rolling(5, min_periods=1).mean())
)

# Fill NA values with global mean K%
global_K_percent = df['K_percent'].mean()
df['opponent_recent_K_percent'] = df['opponent_recent_K_percent'].fillna(global_K_percent)
df['opponent_recent_K_percent_vs_hand'] = df['opponent_recent_K_percent_vs_hand'].fillna(global_K_percent)

# Player-specific averages for missing values
player_means = df.groupby('player')[['walks', 'pitches', 'battersFaced']].mean().to_dict(orient='index')
global_means = df[['walks', 'pitches', 'battersFaced']].mean()

# --- Add opponent_K_percent_season ---
season_k_pct = (
    df.groupby('opponent')[['strikeouts', 'battersFaced']]
    .sum()
    .assign(opponent_K_percent_season=lambda x: x['strikeouts'] / x['battersFaced'])
    .reset_index()
)

# --- Add opponent_K_percent_season_vs_hand ---
season_k_pct_vs_hand = (
    df.groupby(['opponent', 'pitcherHand'])[['strikeouts', 'battersFaced']]
    .sum()
    .assign(opponent_K_percent_season_vs_hand=lambda x: x['strikeouts'] / x['battersFaced'])
    .reset_index()
)

# Merge into main df
df = df.merge(season_k_pct[['opponent', 'opponent_K_percent_season']], on='opponent', how='left')
df = df.merge(
    season_k_pct_vs_hand[['opponent', 'pitcherHand', 'opponent_K_percent_season_vs_hand']],
    on=['opponent', 'pitcherHand'], how='left'
)

# Fill any remaining NA values just in case
df['opponent_K_percent_season'] = df['opponent_K_percent_season'].fillna(global_K_percent)
df['opponent_K_percent_season_vs_hand'] = df['opponent_K_percent_season_vs_hand'].fillna(global_K_percent)


# Features and target
features = [
    'player', 'opponent', 'pitcherHand',
    'walks', 'pitches', 'battersFaced',
    'days_since_start',
    'opponent_recent_K_percent',
    'opponent_recent_K_percent_vs_hand',
    'opponent_K_percent_season',
    'opponent_K_percent_season_vs_hand'
]
target = 'strikeouts'

X = df[features]
y = df[target]

# Encode categorical features
categorical = ['player', 'opponent', 'pitcherHand']
numerical = [
    'walks', 'pitches', 'battersFaced',
    'days_since_start',
    'opponent_recent_K_percent',
    'opponent_recent_K_percent_vs_hand',
    'opponent_K_percent_season',
    'opponent_K_percent_season_vs_hand'
]

encoder = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
encoder.fit(df[categorical])

preprocessor = ColumnTransformer(
    transformers=[
        ('cat', encoder, categorical)
    ],
    remainder='passthrough'
)

# Build pipeline
pipeline = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))
])

pipeline.fit(X, y)

# Save encoded feature names (for advanced use/debugging)
encoded_feature_names = encoder.get_feature_names_out(categorical).tolist()
full_feature_names = encoded_feature_names + numerical

# --- Predict function ---
def predict_strikeouts(player, opponent, pitcherHand, date, walks=None, pitches=None, battersFaced=None):
    date = pd.to_datetime(date)
    days_since_start = (date - start_date).days

    # Impute missing values
    if player in player_means:
        avg = player_means[player]
        walks = walks if walks is not None else avg['walks']
        pitches = pitches if pitches is not None else avg['pitches']
        battersFaced = battersFaced if battersFaced is not None else avg['battersFaced']
    else:
        walks = walks if walks is not None else global_means['walks']
        pitches = pitches if pitches is not None else global_means['pitches']
        battersFaced = battersFaced if battersFaced is not None else global_means['battersFaced']

    # Get opponent recent strikeout rates
    past_games = df[df['opponent'] == opponent].sort_values(by='date')
    k_rates = past_games['K_percent'].rolling(5, min_periods=1).mean().iloc[-1] if not past_games.empty else global_K_percent

    vs_hand_games = df[(df['opponent'] == opponent) & (df['pitcherHand'] == pitcherHand)].sort_values(by='date')
    k_rate_vs_hand = vs_hand_games['K_percent'].rolling(5, min_periods=1).mean().iloc[-1] if not vs_hand_games.empty else global_K_percent

    # Compute opponent_K_percent_season
    season_games = df[df['opponent'] == opponent]
    season_k_rate = (
        season_games['strikeouts'].sum() / season_games['battersFaced'].sum()
        if not season_games.empty else global_K_percent
    )

    # Compute opponent_K_percent_season_vs_hand
    season_vs_hand_games = df[(df['opponent'] == opponent) & (df['pitcherHand'] == pitcherHand)]
    season_k_rate_vs_hand = (
        season_vs_hand_games['strikeouts'].sum() / season_vs_hand_games['battersFaced'].sum()
        if not season_vs_hand_games.empty else global_K_percent
    )

    input_df = pd.DataFrame([{
        'player': player,
        'opponent': opponent,
        'pitcherHand': pitcherHand,
        'walks': walks,
        'pitches': pitches,
        'battersFaced': battersFaced,
        'days_since_start': days_since_start,
        'opponent_recent_K_percent': k_rates,
        'opponent_recent_K_percent_vs_hand': k_rate_vs_hand,
        'opponent_K_percent_season': season_k_rate,
        'opponent_K_percent_season_vs_hand': season_k_rate_vs_hand
        
    }])

    prediction = pipeline.predict(input_df)[0]
    return round(prediction, 2)
