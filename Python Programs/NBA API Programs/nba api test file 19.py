from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

# Define the team's name and season ID
team_name = "Los Angeles Lakers"  # Change this to the desired team name
season_id = "2022-23"  # Change this to the desired season ID

# Get a list of all NBA teams
all_teams = teams.get_teams()

# Find the team's ID based on the team's name
team_id = None
for team in all_teams:
    if team['full_name'] == team_name:
        team_id = team['id']
        break

if team_id is None:
    print(f"Team '{team_name}' not found.")
else:
    # Get team roster for the specified season
    team_roster = commonteamroster.CommonTeamRoster(team_id=team_id, season=season_id)
    team_roster_df = team_roster.get_data_frames()[0]
    
    if len(team_roster_df) > 0:
        print(f"Roster for {team_name} ({season_id}):")
        print(team_roster_df[['PLAYER', 'POSITION']])
    else:
        print(f"No roster information available for {team_name} ({season_id}).")
