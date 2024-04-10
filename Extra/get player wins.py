from nba_api.stats.endpoints import commonplayerinfo, playergamelog, playercareerstats
import time

# Initialize index variable
player_id = 2544

i = 0
# Use a while loop to iterate over player IDs
while i < 1:
    # Create an empty list to store the season IDs for each player
    seasons_played = []

    try:
        # Get career stats for the specified player
        career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
        career_data = career_stats.get_data_frames()[0]

        if not career_data.empty:
            # Extract season IDs and save them to the list
            seasons_played = career_data['SEASON_ID'].tolist()
        else:
            print(f"Player with ID {player_id} not found or no career data available.")
            i += 1  # Move to the next player if data is not available
            continue
    except Exception as e:
        print(f"An error occurred for player with ID {player_id}: {str(e)}")
        i += 1  # Move to the next player if an error occurs
        continue

    career_gw_playoffs = 0
    career_gp_playoffs = 0
    career_gw_regular = 0
    career_gp_regular = 0

    # Remove duplicate seasons
    seasons_played = list(set(seasons_played))

    # Iterate over the season IDs for the current player
    for season_id in seasons_played:
        # Get player info by player_id
        player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
        player_data = player_info.get_data_frames()[0]
        player_name = f"{player_data['FIRST_NAME'].iloc[0]} {player_data['LAST_NAME'].iloc[0]}"

        # Get player's game logs for the specified season (Playoffs)
        game_logs_playoffs = playergamelog.PlayerGameLog(player_id=player_id, season=season_id, season_type_all_star='Playoffs')
        game_logs_data_playoffs = game_logs_playoffs.get_data_frames()[0]

        # Get player's game logs for the specified season (Regular Season)
        game_logs_regular = playergamelog.PlayerGameLog(player_id=player_id, season=season_id, season_type_all_star='Regular Season')
        game_logs_data_regular = game_logs_regular.get_data_frames()[0]

        # Calculate the total games played and won by the player for the specified season (Playoffs)
        total_games_played_playoffs = len(game_logs_data_playoffs)
        total_wins_playoffs = game_logs_data_playoffs['WL'].apply(lambda x: 1 if x == 'W' else 0).sum()

        # Calculate the total games played and won by the player for the specified season (Regular Season)
        total_games_played_regular = len(game_logs_data_regular)
        total_wins_regular = game_logs_data_regular['WL'].apply(lambda x: 1 if x == 'W' else 0).sum()

        # Update career statistics for Playoffs
        career_gw_playoffs += total_wins_playoffs
        career_gp_playoffs += total_games_played_playoffs

        # Update career statistics for Regular Season
        career_gw_regular += total_wins_regular
        career_gp_regular += total_games_played_regular

        # Print career statistics for the current player and season
        print(f"Player {player_name}, Season: {season_id}, Playoffs - Wins: {total_wins_playoffs}, Games Played: {total_games_played_playoffs}, Regular Season - Wins: {total_wins_regular}, Games Played: {total_games_played_regular}")

    # Print overall career statistics
    print(f"Player {player_name}, Playoffs - Total Wins: {career_gw_playoffs}, Total Games Played: {career_gp_playoffs}, Regular Season - Total Wins: {career_gw_regular}, Total Games Played: {career_gp_regular}")
    #time.sleep(2)

    # Increment the index variable for the next player
    i += 1
