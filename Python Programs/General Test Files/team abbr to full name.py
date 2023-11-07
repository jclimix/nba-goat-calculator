from nba_api.stats.static import teams

nba_teams = teams.get_teams()

team_abbr = "CLE"

for team in nba_teams:
    if team['abbreviation'] == team_abbr:
        print(f"The full name of {team_abbr} is: {team['full_name']}")
        break