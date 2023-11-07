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
    career_stats_df = career_stats.get_data_frames()[3]

    if len(career_stats_df) == 0:
        print("No career stats found for the player.")
    else:
        # Calculate effective field goal percentage (eFG%)
        total_fgm = career_stats_df.iloc[0]['FGM']
        total_3pm = career_stats_df.iloc[0]['FG3M']
        total_fga = career_stats_df.iloc[0]['FGA']

        efg_percentage = (total_fgm + 0.5 * total_3pm) / total_fga
        
        # Display effective field goal percentage
        print("Effective Field Goal Percentage for", player_name, ":", efg_percentage)
