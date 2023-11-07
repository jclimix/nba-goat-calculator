from sportsipy.mlb.teams import Teams

def print_most_wins(year, wins):
    most_wins = max(wins, key=wins.get)
    print('%s: %s - %s' % (year, wins[most_wins], most_wins))

for year in range(2000, 2019):
    wins = {}
    for team in Teams(year):
        wins[team.name] = team.wins
    print_most_wins(year, wins)