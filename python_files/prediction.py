from model import predict_strikeouts
import csv

to_predict = [
    ["Kyle Freeland", "L", "MIA", "2025-06-04"],
    ["Cal Quantrill", "R", "COL", "2025-06-04"],
    ["Andrew Abbott", "L", "MIL", "2025-06-04"],
    ["Jose Soriano", "R", "BOS", "2025-06-04"],
    ["Lucas Giolito", "R", "LAA", "2025-06-04"],
    ["Ryan Gusto", "R", "PIT", "2025-06-04"],
    ["Mike Burrows", "R", "HOU", "2025-06-04"],
    ["Matthew Boyd", "L", "WSH", "2025-06-04"],
    ["Mackenzie Gore", "L", "CHC", "2025-06-04"],
    ["Luis Ortiz", "R", "NYY", "2025-06-04"],
    ["Clarke Schmidt", "R", "CLE", "2025-06-04"],
    ["Jose Berrios", "R", "PHI", "2025-06-04"],    
    ["Merrill Kelly", "R", "ATL", "2025-06-04"],
    ["Chris Sale", "R", "ARI", "2025-06-04"],
    ["Shane Baz", "R", "TEX", "2025-06-04"],
    ["Noah Cameron", "L", "STL", "2025-06-04"],
    ["Miles Mikolas", "R", "KC", "2025-06-04"],
    ["Cade Povich", "L", "SEA", "2025-06-04"],
    ["Emerson Hancock", "R", "BAL", "2025-06-04"],
    ["Nick Pivetta", "R", "SF", "2025-06-04"],
    ["Zebby Matthews", "R", "ATH", "2025-06-04"],
    ["Jeffrey Springs", "L", "MIN", "2025-06-04"],
    ["Griffin Canning", "R", "LAD", "2025-06-04"],
    ["Tony Gonsolin", "R", "NYM", "2025-06-04"],
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