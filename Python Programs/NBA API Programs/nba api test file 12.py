from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import math

# Get player ID for the desired player
player_name = "Kareem Abdul-Jabbar"  # Change this to the player's name you're interested in
all_players = players.get_players()
player_info = [player for player in all_players if player['full_name'] == player_name]

if not player_info:
    print("Player not found.")
else:
    player_id = player_info[0]['id']

    # Get career stats for the player
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[0]

    sum_blocks = 0

    i = 0
    skip = 0
    div = 0

    if len(career_stats_df) == 0:
        print("No career stats found for the player.")
    else:
        while i < 20:
            career_blocks = career_stats_df.iloc[i]['BLK']
            career_games = career_stats_df.iloc[i]['GP']
            # Display career blocks
            print("Career Blocks for", player_name, ":", career_blocks)
            print("Career Games for", player_name, ":", career_games)
            i = i + 1
            print(i)

            if math.isnan(career_blocks):
                div = div - 1
                print("Div: ", div)
            else:
                div = div + 1
                print("Div: ", div)

            if math.isnan(career_blocks):
                #code
                a = 1
            else:
                sum_blocks = sum_blocks + career_blocks

            if div < 0:
                skip = skip + 1


            final = sum_blocks / div

    i = skip
    while i < 20:
        career_games = career_games + career_stats_df.iloc[i]['GP']
        i = i + 1
    

    print("Sum Blocks: ", sum_blocks)
    print("Div: ", div)
    print("Final: ", final)
    print("Games: ", career_games)
    print("Skip: ", skip)

        
