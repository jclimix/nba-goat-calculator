from nba_api.stats.static import players
import pandas as pd

def get_all_nba_players():
    # Get all NBA players using the nba_api
    nba_players = players.get_players()

    # Create a DataFrame from the list of players
    df = pd.DataFrame(nba_players)

    return df

# Call the function to get the DataFrame with all NBA players
all_players_df = get_all_nba_players()

# Display the DataFrame
print(all_players_df)
