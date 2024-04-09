from nba_api.stats.endpoints import commonallplayers
import pandas as pd

def get_all_players():
    # Use the commonallplayers endpoint to get information about all NBA players
    all_players_info = commonallplayers.CommonAllPlayers().get_data_frames()[0]

    # Extract relevant columns (PersonId, DisplayName, IsCurrentPlayer)
    if 'IS_CURRENT_PLAYER' in all_players_info.columns:
        players_df = all_players_info[['PERSON_ID', 'DISPLAY_FIRST_LAST', 'IS_CURRENT_PLAYER']]
    else:
        # If the column is not present, create 'IsActive' column with NaN values
        players_df = all_players_info[['PERSON_ID', 'DISPLAY_FIRST_LAST']]
        players_df['IS_CURRENT_PLAYER'] = None

    # Rename columns for clarity
    players_df.columns = ['PersonID', 'PlayerName', 'IsActive']

    return players_df

def main():
    # Get all NBA players and their active status
    all_players_df = get_all_players()

    # Display the DataFrame
    print(all_players_df)

if __name__ == "__main__":
    main()
