from model import predict_strikeouts
import csv

to_predict = [
    ["Brandon Pfaadt", "R", "ATL", "2025-06-04"],
    ["Grant Holmes", "R", "ARI", "2025-06-04"],
    ["Noah Cameron", "R", "STL", "2025-06-04"],
    ["Miles Mikolas", "R", "KC", "2025-06-04"],
    ["Casey Mize", "R", "CWS", "2025-06-04"],
    ["Sean Burke", "R", "DET", "2025-06-04"],
    ["Jesus Luzardo", "L", "TOR", "2025-06-04"],
    ["Chris Bassitt", "R", "PHI", "2025-06-04"],
    ["Zach Eflin", "R", "SEA", "2025-06-04"],
    ["Bryan Woo", "R", "BAL", "2025-06-04"],
    ["Dylan Cease", "R", "SF", "2025-06-04"],
    ["Robbie Ray", "L", "SD", "2025-06-04"],
    ["David Peterson", "L", "LAD", "2025-06-04"],
    ["Landon Knack", "R", "NYM", "2025-06-04"],
    ["Framber Valdez", "L", "PIT", "2025-06-04"],
    ["Mitch Keller", "R", "HOU", "2025-06-04"],
    ["Jake Irvin","R","CHC","2025-06-04"],
    ["Slade Cecconi","R","NYY","2025-06-04"],
    ["Max Fried","L","CLE","2025-06-04"],
    ["Jack Leiter","R","TB","2025-06-04"],
    ["Ryan Pepiot","R","TEX","2025-06-04"],
    ["Cole Ragans","L","STL","2025-06-04"],
    ["Matthew Liberatore","L","KC","2025-06-04"]
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