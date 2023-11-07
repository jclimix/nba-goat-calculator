from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import math

# Get player ID for the desired player
player_name = "Zaid Abdul-Aziz"  # Change this to the player's name you're interested in
all_players = players.get_players()
player_info = [player for player in all_players if player['full_name'] == player_name]

if not player_info:
    print("Player not found.")
else:
    player_id = player_info[0]['id']

    # Get career stats for the player
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[0]

    career_length = (len(career_stats_df))
    years = career_length

    sum_blocks = 0
    i = 0
    skip = 0
    all_games = 0

    if len(career_stats_df) == 0:
        print("No career stats found for the player.")
    else:
        while i < years:
            career_blocks = career_stats_df.iloc[i]['BLK']
            career_games = career_stats_df.iloc[i]['GP']
            # Display career blocks
            print("Career Blocks for", player_name, ":", career_blocks)
            print("Career Games for", player_name, ":", career_games)
            i = i + 1
            print(i)

            if math.isnan(career_blocks):
                skip = skip + 1
            else:
                sum_blocks = sum_blocks + career_blocks
                all_games = all_games + career_games
            

    avg_blocks = sum_blocks / all_games
    

    print("Sum Blocks: ", sum_blocks)
    print("Avg Blocks: ", avg_blocks)
    print("Games: ", all_games)
    print("Skip: ", skip)
