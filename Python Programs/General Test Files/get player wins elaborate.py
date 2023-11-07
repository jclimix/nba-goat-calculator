from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.static import teams
from nba_api.stats.endpoints import TeamYearByYearStats

player_id = 2544  # Example player_id (LeBron James)

# Separate script -- TEAM ABBR TO FULL NAME

team_abbreviations = []  # Initialize an empty list to store the team abbreviations
seasons_played = []  # Initialize an empty list to store the seasons played
career_reg_wins = 0
career_reg_games = 0

try:
    career_stats = PlayerCareerStats(player_id=player_id)
    career_data = career_stats.get_data_frames()[0]

    if not career_data.empty:
        selected_columns = career_data[['TEAM_ABBREVIATION', 'SEASON_ID']]
        # Extract and store team abbreviations and seasons played in the list
        team_abbreviations = selected_columns['TEAM_ABBREVIATION'].tolist()
        seasons_played = selected_columns['SEASON_ID'].tolist()
    else:
        print("Player not found or no career data available for the provided player ID.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Now, you can use the 'team_abbreviations' list to access the saved team abbreviations
#print("Team Abbreviations:", team_abbreviations)

# Separate script

nba_teams = teams.get_teams()

# Initialize an empty dictionary to store team names
team_names = {}

# Iterate over the indices and team abbreviations
for i, team_abbr in enumerate(team_abbreviations):
    for team in nba_teams:
        if team['abbreviation'] == team_abbr:
            team_names[i] = team['full_name']
            #print(f"{team_abbr}: {team['full_name']}")
            break

# Iterate over the team names and seasons played
for i, team_name in team_names.items():
    season_id = seasons_played[i]

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
            
            career_reg_wins += wins
            career_reg_games += games_played

            #print(f"{team_name} had {wins} wins out of {games_played} games played in the {season_id} season.")

print(f"{player_id}: {career_reg_wins} wins out of {career_reg_games} games.")
