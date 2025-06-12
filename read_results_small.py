'''
Notes
- The file results.csv has been exported using LibreOffice.
'''

import csv
from datetime import datetime


matches = []

with open('results.csv', mode='r') as file:
    # Reading the CSV file
    csvFile = csv.reader(file)
    
    # Skipping the header (uncomment if needed)
    line = next(csvFile)
    # print(line)
    # print(line[0])
    hometeam_vs_awayteam = line[0]
    (hometeam, _, awayteam) = hometeam_vs_awayteam.split(" ")
    # print(hometeam)
    # print(awayteam)

    

    # Displaying the contents of the CSV file
    for line in csvFile:
        # print(line)
        date = datetime.strptime(line[1], '%d.%m.%Y')
        # print(date)

        home_team = line[3]
        if home_team=="Atalanta":
            away_team = "Parma"
        else:
            away_team = "Atalanta"

        home_goals = int(line[4])
        # print(home_goals)
        away_goals = int(line[5])
        # print(away_goals)



        match = { "date": date, "home_team": home_team, "away_team": away_team, "home_goals": home_goals, "away_goals": away_goals }
        # print(match)
        matches.append(match)


print(matches)

# Wie oft hat Atalanta gewonnen?
wins = 0
draws = 0
losses = 0
goals_atalanta = 0
goals_parma = 0

for match in matches:
    result = match["home_goals"]-match["away_goals"]

    # goals
    if match["home_team"]=="Atalanta":
        goals_atalanta += match["home_goals"]
        goals_parma += match["away_goals"]
    else:
        goals_atalanta += match["away_goals"]
        goals_parma += match["home_goals"]

    if result == 0:
        draws += 1
    elif result > 0:
        if match["home_team"]=="Atalanta":
            wins += 1
        else:
            losses += 1

    else: # result < 0
        if match["away_team"]=="Atalanta":
            wins += 1
        else:
            losses += 1
print("Atalanta:", wins, "wins,", draws, "draws,", losses, "loses.")                
print("Atalanta: goals", goals_atalanta, "goals average", goals_atalanta/len(matches))



