#Import everything
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import math, time

size = 21
players_id = [0] * size

players_id[0] = 76001
players_id[1] = 76002
players_id[2] = 76003
players_id[3] = 51
players_id[4] = 1505
players_id[5] = 949
players_id[6] = 76005
players_id[7] = 76006
players_id[8] = 76007
players_id[9] = 203518
players_id[10] = 1630173
players_id[11] = 101165
players_id[12] = 76008
players_id[13] = 76009
players_id[14] = 76010
players_id[15] = 203112
players_id[16] = 76011
players_id[17] = 76012
players_id[18] = 200801
players_id[19] = 1629121
players_id[20] = 203919

# Get a list of all players
all_players = players.get_players()

# Print Column Headers
print("PLAYER_ID, PLAYER_NAME, PPG, APG, RPG, SPG, BPG, FG, eFG, TS")

a = 11

# Iterate through each player and fetch their career stats
while a < size:

    player_id = players_id[a]

    # Get REGULAR career stats for the player

    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[0]

    player_info = [player for player in all_players if player['id'] == player_id]
    player_name = player_info[0]['full_name']

    # Get Regular Season Stats

    career_length = (len(career_stats_df))
    years = career_length

    print(career_stats_df)
    a = a + 1