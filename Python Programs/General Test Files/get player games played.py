from nba_api.stats.endpoints import commonplayerinfo, playercareerstats
from nba_api.stats.static import players

# Function to get a player's career statistics for SEASON_ID and TEAM_ABBREVIATION
def get_career_season_team(player_id):
    # Get player info by ID
    player_info = commonplayerinfo.CommonPlayerInfo(player_id=player_id)
    player_info = player_info.get_data_frames()[0]

    # Extract player's full name
    player_name = player_info['DISPLAY_FIRST_LAST'][0]

    # Get player's career statistics
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats = career_stats.get_data_frames()[0]

    # Select only the SEASON_ID and TEAM_ABBREVIATION columns
    career_season_team = career_stats[['SEASON_ID', 'TEAM_ABBREVIATION']]

    return career_season_team

# Function to find player ID by player name
def find_player_id(player_name):
    player_list = players.find_players_by_full_name(player_name)
    if player_list:
        return player_list[0]['id']
    else:
        return None

# Example usage
if __name__ == "__main__":
    player_name = "LeBron James"  # Replace with the player's name you want to query
    player_id = find_player_id(player_name)

    if player_id is not None:
        career_season_team = get_career_season_team(player_id)
        print(f"SEASON_ID and TEAM_ABBREVIATION for {player_name} (Player ID: {player_id}):")
        print(career_season_team)
    else:
        print(f"Player '{player_name}' not found.")
