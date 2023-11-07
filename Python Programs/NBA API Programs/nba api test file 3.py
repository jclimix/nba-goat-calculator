from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Get player ID for the desired player
player_name = "LeBron James"
all_players = players.get_players()
player_info = [player for player in all_players if player['full_name'] == player_name]

if not player_info:
    print("Player not found.")
else:
    player_id = player_info[0]['id']

    # Get career stats for the player
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[0]

    if len(career_stats_df) == 0:
        print("No career stats found for the player.")
    else:
        # Calculate career averages
        career_averages = career_stats_df.iloc[0]
        ppg = career_averages['PTS'] / career_averages['GP']
        apg = career_averages['AST'] / career_averages['GP']
        rpg = career_averages['REB'] / career_averages['GP']
        
        # Display career averages
        print("Career averages for", player_name, ":")
        print("Points per game:", ppg)
        print("Assists per game:", apg)
        print("Rebounds per game:", rpg)
        # You can add more stats as needed
