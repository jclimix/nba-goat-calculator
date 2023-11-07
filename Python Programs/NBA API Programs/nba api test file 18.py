from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

# Define the season ID (e.g., 2022-23) and team ID (e.g., 1610612744 for Golden State Warriors)
season_id = "1949-50"  # Change this to the desired season ID
team_id = 1610612747   # Change this to the desired team ID

# Get team roster for the specified season and team
team_roster = commonteamroster.CommonTeamRoster(team_id=team_id, season=season_id)
team_roster_df = team_roster.get_data_frames()[0]

all_teams = teams.get_teams()
team_info = [team for team in all_teams if team['id'] == team_id]


if len(team_roster_df) == 0:
    print("No roster information available for the specified season and team.")
else:
    
    team_name = team_info[0]['full_name']
        
    print("Season:", season_id)
    print("Team:", team_name)
    print("Team ID:", team_id)
    #print(team_roster_df)

    i = 0

    while i < len(team_roster_df):
        player_name = team_roster_df.iloc[i]['PLAYER']
        player_id = team_roster_df.iloc[i]['PLAYER_ID']
        print(f"{player_id}, {player_name}, {team_name}, {team_id}, {season_id}")
        i = i + 1
