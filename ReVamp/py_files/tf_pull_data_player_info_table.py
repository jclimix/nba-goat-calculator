from nba_api.stats.endpoints import commonallplayers
import pandas as pd
import os

def get_all_nba_players():
    # Fetching data from NBA API
    all_players_data = commonallplayers.CommonAllPlayers()
    all_players_info = all_players_data.get_data_frames()[0]

    # Extracting relevant columns
    relevant_columns = ['PERSON_ID', 'DISPLAY_FIRST_LAST']
    df = all_players_info[relevant_columns]

    # Renaming columns
    df.columns = ['PLAYER_ID', 'PLAYER_NAME']

    return df

def get_nba_players_info():
    # Fetching data from NBA API
    players_data = commonallplayers.CommonAllPlayers(is_only_current_season=1)
    players_info = players_data.get_data_frames()[0]

    # Extracting relevant columns
    relevant_columns = ['PERSON_ID', 'DISPLAY_FIRST_LAST', 'ROSTERSTATUS']
    df = players_info[relevant_columns]

    # Renaming columns
    df.columns = ['PLAYER_ID', 'PLAYER_NAME', 'ACTIVE_STATUS']

    return df

def compare_players_status(all_players_df, current_players_df):
    # Create a new DataFrame with "ACTIVE_STATUS" column
    final_df = all_players_df.copy()
    final_df['ACTIVE_STATUS'] = 0  # Initialize with 0 for all players

    # Iterate through each player in the all_players_df
    for index, player_row in all_players_df.iterrows():
        player_id = player_row['PLAYER_ID']

        # Check if the player is in the current NBA players DataFrame
        if player_id in current_players_df['PLAYER_ID'].values:
            final_df.loc[final_df['PLAYER_ID'] == player_id, 'ACTIVE_STATUS'] = 1
            # If found in current players, set ACTIVE_STATUS to 1 and break the loop

    return final_df

if __name__ == "__main__":
    # Get all NBA players
    all_nba_players_df = get_all_nba_players()

    # Get current NBA players
    current_nba_players_df = get_nba_players_info()

    # Compare players' status and create a new df
    final_df = compare_players_status(all_nba_players_df, current_nba_players_df)

    print(final_df.head())


    output_directory = '../csv_files'

    output_path = os.path.join(os.path.dirname(__file__), output_directory, 'final_player_info.csv')

    # Check if the directory exists, create it if not
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    final_df.to_csv(output_path, index=False)
    print("Result DataFrame saved to final_player_info.csv")
