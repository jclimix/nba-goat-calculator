from nba_api.stats.endpoints import commonallplayers
import pandas as pd

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

if __name__ == "__main__":
    # Calling the function to get NBA players info
    nba_players_df = get_nba_players_info()

    # Displaying the DataFrame
    print(nba_players_df.head())

    # Save the DataFrame to a CSV file
    nba_players_df.to_csv('nba_players_info.csv', index=False)
    print("DataFrame saved to nba_players_info.csv")
