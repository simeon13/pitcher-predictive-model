from model import predict_strikeouts
import csv

to_predict = [
    ["Edward Cabrera", "R", "TB", "2025-06-06"],
    ["Zack Littell", "R", "MIA", "2025-06-06"],
    ["Bailey Falter", "L", "PHI", "2025-06-06"],
    ["Patrick Corbin", "L", "WSH", "2025-06-06"],
    ["Michael Soroka", "R", "TEX", "2025-06-06"],
    ["Walker Buehler", "R", "NYY", "2025-06-06"],
    ["Will Warren", "R", "BOS", "2025-06-06"],
    ["Eduardo Rodriguez", "L", "CIN", "2025-06-06"],
    ["Nick Lodolo", "L", "ARI", "2025-06-06"],
    ["Ben Brown", "R", "DET", "2025-06-06"],
    ["Tarik Skubal", "L", "CHC", "2025-06-06"],
    ["Colton Gordon", "L", "CLE", "2025-06-06"],
    ["Logan Allen", "L", "HOU", "2025-06-06"],
    ["Seth Lugo", "R", "CHW", "2025-06-06"],
    ["Davis Martin", "R", "KC", "2025-06-06"],
    ["Randy Vasquez", "R", "MIL", "2025-06-06"],
    ["Chad Patrick", "R", "SD", "2025-06-06"],
    ["Bailey Ober", "R", "TOR", "2025-06-06"],
    ["Sonny Gray", "R", "LAD", "2025-06-06"],
    ["Kodai Senga", "R", "COL", "2025-06-06"],
    ["Antonio Senzatela", "R", "NYM", "2025-06-06"],
    ["Bryce Miller", "R", "LAA", "2025-06-06"],
    ["Kyle Hendricks", "R", "SEA", "2025-06-06"],
    ["Dean Kremer", "R", "ATH", "2025-06-06"],
    ["JP Sears", "L", "BAL", "2025-06-06"],
    ["Spencer Schwellenbach", "R", "SF", "2025-06-06"],
    ["Hayden Birdsong", "R", "ATL", "2025-06-06"]
]


# Open a CSV file for writing
with open('assets/results.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Player', 'Opp', 'Prediction'])

    # Loop through predictions and write each to CSV
    for prediction in to_predict:
        player, pitcher_hand, opponent, date = prediction
        strikeouts = predict_strikeouts(player, opponent, pitcher_hand, date)
        writer.writerow([player, opponent, strikeouts])