from nba_api.stats.endpoints import PlayerCareerStats

player_id = 2544

try:
    career_stats = PlayerCareerStats(player_id=player_id)
    career_data = career_stats.get_data_frames()[0]
    
    if not career_data.empty:
        selected_columns = career_data[['TEAM_ABBREVIATION', 'SEASON_ID']]
        print(selected_columns)
    else:
        print("Player not found or no career data available for the provided player ID.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
