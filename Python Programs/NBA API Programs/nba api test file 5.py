from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Get player ID for LeBron James
player_name = "LeBron James"
all_players = players.get_players()
player_info = [player for player in all_players if player['full_name'] == player_name]

if not player_info:
    print("Player not found.")
else:
    player_id = player_info[0]['id']

    # Get career stats for LeBron James
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[3]

    if len(career_stats_df) == 0:
        print("No career stats found for the player.")
    else:
        # Calculate and display points per game (PPG) throughout career
        career_stats_df['PPG'] = career_stats_df['PTS'] / career_stats_df['GP']
        career_stats_df['Career_PPG'] = career_stats_df.PPG.mean()        
        print("LeBron James' points per game throughout his career:")
        print(career_stats_df[['SEASON_ID', 'PPG', 'Career_PPG']])
