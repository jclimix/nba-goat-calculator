from nba_api.stats.endpoints import PlayerCareerStats
from nba_api.stats.static import players
import pandas as pd

# Define the list of player IDs
player_ids = [2544,201939]

timeout_value = 100

# Set i
i = 0

while i < len(player_ids):

    reg_off_reb = 0
    reg_def_reb = 0
    ply_off_reb = 0
    ply_def_reb = 0

    # Replace 'PLAYER_ID' with the actual player ID you want to retrieve career stats for
    player_id = player_ids[i]

    # Get player information
    player_info = players.find_player_by_id(player_id)

    if player_info is None:
        print(f"Player with ID {player_id} not found.")
    else:
        player_name = player_info['full_name']


        # Get career regular season averages for the player
        career_stats = PlayerCareerStats(player_id=player_id, per_mode36='PerGame',timeout=timeout_value)
        career_stats_df = career_stats.get_data_frames()[1]

        # Get career playoffs averages for the player
        career_stats2 = PlayerCareerStats(player_id=player_id, per_mode36='PerGame',timeout=timeout_value)
        career_stats_df2 = career_stats.get_data_frames()[3]

        if not career_stats_df.empty:

            if career_stats_df['OREB'].values[0] is not None:

                reg_off_reb = career_stats_df['OREB'].values[0]

            if career_stats_df['DREB'].values[0] is not None:

                reg_def_reb = career_stats_df['DREB'].values[0]

        if not career_stats_df2.empty:

            if career_stats_df2['OREB'].values[0] is not None:

                ply_off_reb = career_stats_df2['OREB'].values[0]

            if career_stats_df2['DREB'].values[0] is not None:

                ply_def_reb = career_stats_df2['DREB'].values[0]

        print(f"{i},{player_id},{player_name},{reg_off_reb},{reg_def_reb},{ply_off_reb},{ply_def_reb}")

    i = i + 1