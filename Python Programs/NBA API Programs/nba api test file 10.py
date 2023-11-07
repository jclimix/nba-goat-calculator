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
    career_stats_df = career_stats.get_data_frames()[1]

    if len(career_stats_df) == 0:
        print("No career stats found for the player.")
    else:
        # Calculate Player Efficiency Rating (PER)
        total_points = career_stats_df.iloc[0]['PTS']
        total_rebounds = career_stats_df.iloc[0]['REB']
        total_assists = career_stats_df.iloc[0]['AST']
        total_steals = career_stats_df.iloc[0]['STL']
        total_blocks = career_stats_df.iloc[0]['BLK']
        total_turnovers = career_stats_df.iloc[0]['TOV']
        total_fgm = career_stats_df.iloc[0]['FGM']
        total_3pm = career_stats_df.iloc[0]['FG3M']
        total_fga = career_stats_df.iloc[0]['FGA']
        total_fta = career_stats_df.iloc[0]['FTA']
        total_ftm = career_stats_df.iloc[0]['FTM']

        min_per_game = career_stats_df.iloc[0]['MIN'] / career_stats_df.iloc[0]['GP']
        
        per = (
            (total_points + total_rebounds + total_assists + total_steals + total_blocks)
            - (total_fga - total_fgm)
            - (total_fta - total_ftm)
            - total_turnovers
        ) * (15 / min_per_game)
        
        # Display Player Efficiency Rating
        print("Player Efficiency Rating for", player_name, ":", per)
