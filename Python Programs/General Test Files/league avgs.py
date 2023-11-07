from nba_api.stats.static import players
from nba_api.stats.endpoints import playergamelog
import pandas as pd
import concurrent.futures

# Function to calculate the average points per game for a given season
def get_average_ppg_for_player(player_info, season):
    player_id = player_info['id']
    player_name = f"{player_info['first_name']} {player_info['last_name']}"

    # Get the player's game log for the specified season
    game_log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    game_log_df = game_log.get_data_frames()[0]

    # Calculate the average points per game
    average_ppg = game_log_df['PTS'].mean()

    return {'Player': player_name, 'Average Points Per Game': average_ppg}

# Define the season you want to analyze (e.g., '2022-23' for the 2022-2023 NBA season)
season_to_analyze = '2022-23'

# Get a list of all NBA players
all_nba_players = players.get_players()

# Create an empty list to store player stats
player_stats = []

# Use concurrent processing to speed up data retrieval
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_average_ppg_for_player, player_info, season_to_analyze) for player_info in all_nba_players]
    
    # Collect results
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        player_stats.append(result)

# Create a DataFrame from the list of player stats
player_stats_df = pd.DataFrame(player_stats)

# Sort the DataFrame by average points per game in descending order
player_stats_df = player_stats_df.sort_values(by='Average Points Per Game', ascending=False)

# Print the DataFrame with player names and average points per game
print(player_stats_df)
