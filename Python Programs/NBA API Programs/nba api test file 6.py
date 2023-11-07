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

    # Get career REG stats for LeBron James
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[1]  #Index 1 = Reagular Season Totals

    # Get career REG stats for LeBron James
    career_stats2 = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_df2 = career_stats2.get_data_frames()[3]  #Index 3 = PostSeason Totals

    if len(career_stats_df) == 0:
        print("No postseason stats found for the player.")
    else:
        # Display LeBron James' postseason stats
        print("LeBron James' REG stats:")
        print(career_stats_df)
        print("LeBron James' POST stats:")
        print(career_stats_df2)

