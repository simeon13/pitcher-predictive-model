from model import predict_strikeouts
import csv

to_predict = [
    ["Sandy Alcantara", "R", "COL", "2025-06-03"],
    ["Lance McCullers Jr", "R", "PIT", "2025-06-03"],
    ["Paul Skenes", "R", "HOU", "2025-06-03"],
    ["Cade Horton", "R", "WSH", "2025-06-03"],
    ["Trevor Williams", "R", "CHC", "2025-06-03"],
    ["Tanner Bibee", "R", "NYY", "2025-06-03"],
    ["Carlos Rodon", "L", "CLE", "2025-06-03"],
    ["Cristopher Sanchez", "L", "TOR", "2025-06-03"],
    ["Bowden Francis", "R", "PHI", "2025-06-03"],
    ["Yusei Kikuchi", "L", "BOS", "2025-06-03"],
    ["Brayan Bello", "R", "LAA", "2025-06-03"],    
    ["Freddy Peralta", "R", "CIN", "2025-06-03"],
    ["Hunter Greene", "R", "MIL", "2025-06-03"],
    ["Zac Gallen", "R", "ATL", "2025-06-03"],
    ["Spencer Strider", "R", "ARI", "2025-06-03"],
    ["Tyler Mahle", "R", "TB", "2025-06-03"],
    ["Drew Rasmussen", "R", "TEX", "2025-06-03"],
    ["Shane Smith", "R", "DET", "2025-06-03"],
    ["Michael Lorenzen", "R", "STL", "2025-06-03"],
    ["Andre Pallante", "R", "KC", "2025-06-03"],
    ["Tomoyuki Sugano", "R", "SEA", "2025-06-03"],
    ["George Kirby", "R", "BAL", "2025-06-03"],
    ["Landen Roupp", "R", "SD", "2025-06-03"],
    ["Pablo Lopez", "R", "ATH", "2025-06-03"],
    ["Jacob Lopez", "R", "MIN", "2025-06-03"],
    ["Tylor Megill", "R", "LAD", "2025-06-03"]
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