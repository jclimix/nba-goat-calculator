from nba_api.stats.endpoints import TeamYearByYearStats
from nba_api.stats.static import teams

# Input team name and season ID
team_name = "Los Angeles Lakers"  # Replace with the desired team name
season_id = "2022-23"             # Replace with the desired season ID

# Get the team ID based on the team name
team_info = teams.find_teams_by_full_name(team_name)
if not team_info:
    print(f"Team '{team_name}' not found.")
else:
    team_id = team_info[0]['id']

    # Create a TeamYearByYearStats instance
    team_stats = TeamYearByYearStats(team_id=team_id, season_type_all_star="Regular Season")

    # Fetch the data
    team_stats_data = team_stats.get_data_frames()[0]

    # Filter the data for the specified season
    filtered_data = team_stats_data[team_stats_data['YEAR'] == season_id]

    if not filtered_data.empty:
        wins = filtered_data['WINS'].values[0]
        games_played = filtered_data['GP'].values[0]
        print(f"{team_name} had {wins} wins out of {games_played} games played in the {season_id} season.")
    else:
        print(f"Team '{team_name}' not found in the {season_id} season.")
