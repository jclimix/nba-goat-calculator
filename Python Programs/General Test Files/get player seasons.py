from nba_api.stats.endpoints import PlayerCareerStats

# Define the player ID (replace with the desired player's ID)
player_id = 2544  # Example player ID for LeBron James

# Create an empty list to store the season IDs
seasons_played = []

try:
    # Get career stats for the specified player
    career_stats = PlayerCareerStats(player_id=player_id)
    career_data = career_stats.get_data_frames()[0]

    if not career_data.empty:
        # Extract season IDs and save them to the list
        seasons_played = career_data['SEASON_ID'].tolist()
    else:
        print("Player not found or no career data available for the provided player ID.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Print the array of season IDs
print("Seasons Played:", seasons_played)
