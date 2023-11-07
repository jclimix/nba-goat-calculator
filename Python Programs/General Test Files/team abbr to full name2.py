from nba_api.stats.endpoints import PlayerCareerStats

player_id = 2544

team_abbreviations = []  # Initialize an empty list to store the team abbreviations

try:
    career_stats = PlayerCareerStats(player_id=player_id)
    career_data = career_stats.get_data_frames()[0]

    if not career_data.empty:
        selected_columns = career_data[['TEAM_ABBREVIATION', 'SEASON_ID']]
        print(selected_columns)

        # Extract and store team abbreviations in the list
        team_abbreviations = selected_columns['TEAM_ABBREVIATION'].tolist()
        
    else:
        print("Player not found or no career data available for the provided player ID.")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# Now, you can use the 'team_abbreviations' list to access the saved team abbreviations
print("Team Abbreviations:", team_abbreviations)
