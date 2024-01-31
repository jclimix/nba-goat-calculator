#get a players career stats

from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

def get_career_stats(player_id):
    # Fetch player career stats from NBA API;
    # Use mode "PerGame" to get player averages per game. Use index "1" to get single row that contains 
    # averages for every season played by the selected player.
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id, per_mode36='PerGame').get_data_frames()[1]

    # Display player name
    player_name = get_player_name(player_id)
    print(f"Career Stats for {player_name} (Player ID {player_id}):")
    
    # Display career stats
    print(career_stats)

def get_player_name(player_id):
    # Fetch player information from NBA API
    player_info = players.find_player_by_id(player_id)
    return player_info['full_name']

if __name__ == '__main__':
    #LeBron James
    player_id = 2544
    
    get_career_stats(player_id)


