import json
import os
import csv


from pydfs_lineup_optimizer import get_optimizer, Site, Sport
optimizer = get_optimizer(Site.DRAFTKINGS_CAPTAIN_MODE, Sport.FOOTBALL)

#If there is a fail here, watch out for empty strings in the csv, as they will cause the parser to search too far
optimizer.load_players_from_csv("../SD_Proj.csv")

N=50
lineups = optimizer.optimize(n=N)



# Specify the file name for the CSV export
csv_filename = 'lineups.csv'

# Export lineups to a CSV file
with open(csv_filename, 'w', newline='') as csvfile:
    lineup_writer = csv.writer(csvfile)
    
    # Write the header row with column names
    lineup_writer.writerow(['CPTN', 'FLEX', 'FLEX', 'FLEX', 'FLEX', 'FLEX'])

    # Write each lineup to the CSV file
    for lineup in lineups:
        lineup_writer.writerow([player.full_name for player in lineup.players])

print(f"Lineups exported to {csv_filename}")











