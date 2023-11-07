#Import everything
from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import math

# Get a list of all players
all_players = players.get_players()

# Get player ID for the desired player
player_name = "LeBron James"  # Change this to the player's name you're interested in
all_players = players.get_players()
player_info = [player for player in all_players if player['full_name'] == player_name]

player_id = player_info[0]['id']

# Print Player Info
print("Player ID: ", player_id)
print("Player Name: ", player_name)

# Get REGULAR career stats for the player

career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
career_stats_df = career_stats.get_data_frames()[0]

# Get Regular Season Stats

career_length = (len(career_stats_df))
years = career_length

#variables

R_sum_points = 0
R_sum_assists = 0
R_sum_blocks = 0
R_sum_steals = 0
R_sum_rebounds = 0
R_sum_fta = 0

R_sum_fgm = 0
R_sum_fga = 0

R_sum_3fgm = 0

R_valid_games = 0
R_valid_games_reb = 0
all_games = 0
skip = 0
i = 0

while i < years:
        
        career_points = career_stats_df.iloc[i]['PTS']
        career_assists = career_stats_df.iloc[i]['AST']
        career_rebounds = career_stats_df.iloc[i]['REB']
        career_blocks = career_stats_df.iloc[i]['BLK']
        career_steals = career_stats_df.iloc[i]['STL']
        career_games = career_stats_df.iloc[i]['GP']
        career_3pm = career_stats_df.iloc[i]['FG3M']
        career_fgm = career_stats_df.iloc[i]['FGM']
        career_fga = career_stats_df.iloc[i]['FGA']
        career_fta = career_stats_df.iloc[i]['FTA']

        R_sum_fgm = R_sum_fgm + career_fgm
        R_sum_fga = R_sum_fga + career_fga
        R_sum_fta = R_sum_fta + career_fta

        if career_3pm is not None:
            if math.isnan(career_3pm):
                R_sum_3fgm = R_sum_3fgm + 0
            else:
                R_sum_3fgm = R_sum_3fgm + career_3pm

        i = i + 1

        all_games = all_games + career_games

        # Find Career Points
        R_sum_points = R_sum_points + career_points

        # Find Career Assists
        R_sum_assists = R_sum_assists + career_assists

        # Find Career Rebounds (1951)
        if career_rebounds is not None:
            if math.isnan(career_rebounds):   
                skip = skip + 1
            else:
                R_sum_rebounds = R_sum_rebounds + career_rebounds
                R_valid_games_reb = R_valid_games_reb + career_games
        else:
                R_valid_games_reb = R_valid_games_reb + career_games

        # Find Career Blocks and Steals (1974)
        if career_blocks is not None:
            if math.isnan(career_blocks):   
                skip = skip + 1
            else:
                R_sum_blocks = R_sum_blocks + career_blocks
                R_sum_steals = R_sum_steals + career_steals
                R_valid_games = R_valid_games + career_games
        else:
                R_valid_games = R_valid_games + career_games
        
R_avg_pts = R_sum_points / all_games
R_avg_ast = R_sum_assists / all_games
R_avg_reb = R_sum_rebounds / R_valid_games_reb
R_avg_blocks = R_sum_blocks / R_valid_games
R_avg_steals = R_sum_steals / R_valid_games
R_avg_fg = R_sum_fgm / R_sum_fga

if R_sum_3fgm == None:
        R_sum_3fgm = 0

R_avg_efg = ((R_sum_fgm + (0.5 * R_sum_3fgm)) / R_sum_fga)
R_avg_ts = (R_sum_points) / (2 * (R_sum_fga + 0.44 * R_sum_fta))

# Round the REG Stats
R_avg_pts = round(R_avg_pts, 1)
R_avg_ast = round(R_avg_ast, 1)
R_avg_reb = round(R_avg_reb, 1)
R_avg_steals = round(R_avg_steals, 1)
R_avg_blocks = round(R_avg_blocks, 1)
R_avg_fg = round(R_avg_fg, 3)
R_avg_efg = round(R_avg_efg, 3)
R_avg_ts = round(R_avg_ts, 3)

print("REG Career Avg Points: ", R_avg_pts)
print("REG Career Avg Assists: ", R_avg_ast)
print("REG Career Avg Rebounds: ", R_avg_reb)
print("REG Career Avg Steals: ", R_avg_steals)
print("REG Career Avg Blocks: ", R_avg_blocks)
print("REG Career Field Goal %: ", R_avg_fg)
print("REG Career e-Field Goal %: ", R_avg_efg)
print("REG Career True Shooting %: ", R_avg_ts)

# Get PLAYOFF career stats for the player

career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
career_stats_df = career_stats.get_data_frames()[2]

# Get Regular Season Stats

career_length = (len(career_stats_df))
playoff_runs = career_length

#variables

P_sum_points = 0
P_sum_assists = 0
P_sum_blocks = 0
P_sum_steals = 0
P_sum_rebounds = 0
P_sum_fta = 0

P_sum_fgm = 0
P_sum_fga = 0

P_sum_3fgm = 0

P_valid_games = 0
P_valid_games_reb = 0
all_games = 0
skip = 0
i = 0

while i < playoff_runs:
        
        career_points = career_stats_df.iloc[i]['PTS']
        career_assists = career_stats_df.iloc[i]['AST']
        career_rebounds = career_stats_df.iloc[i]['REB']
        career_blocks = career_stats_df.iloc[i]['BLK']
        career_steals = career_stats_df.iloc[i]['STL']
        career_games = career_stats_df.iloc[i]['GP']
        career_3pm = career_stats_df.iloc[i]['FG3M']
        career_fgm = career_stats_df.iloc[i]['FGM']
        career_fga = career_stats_df.iloc[i]['FGA']
        career_fta = career_stats_df.iloc[i]['FTA']

        P_sum_fgm = P_sum_fgm + career_fgm
        P_sum_fga = P_sum_fga + career_fga
        P_sum_fta = P_sum_fta + career_fta

        if career_3pm is not None:
            if math.isnan(career_3pm):
                P_sum_3fgm = P_sum_3fgm + 0
            else:
                P_sum_3fgm = P_sum_3fgm + career_3pm

        i = i + 1

        all_games = all_games + career_games

        # Find Career Points
        P_sum_points = P_sum_points + career_points

        # Find Career Assists
        P_sum_assists = P_sum_assists + career_assists

        # Find Career Rebounds (1951)
        if career_rebounds is not None:
            if math.isnan(career_rebounds):   
                skip = skip + 1
            else:
                P_sum_rebounds = P_sum_rebounds + career_rebounds
                P_valid_games_reb = P_valid_games_reb + career_games
        else:
                P_valid_games_reb = P_valid_games_reb + career_games

        # Find Career Blocks and Steals (1974)
        if career_blocks is not None:
            if math.isnan(career_blocks):   
                skip = skip + 1
            else:
                P_sum_blocks = P_sum_blocks + career_blocks
                P_sum_steals = P_sum_steals + career_steals
                P_valid_games = P_valid_games + career_games
        else:
                P_valid_games = P_valid_games + career_games
        
P_avg_pts = P_sum_points / all_games
P_avg_ast = P_sum_assists / all_games
P_avg_reb = P_sum_rebounds / P_valid_games_reb
P_avg_blocks = P_sum_blocks / P_valid_games
P_avg_steals = P_sum_steals / P_valid_games
P_avg_fg = P_sum_fgm / P_sum_fga

if P_sum_3fgm == None:
        P_sum_3fgm = 0

P_avg_efg = ((P_sum_fgm + (0.5 * P_sum_3fgm)) / P_sum_fga)
P_avg_ts = (P_sum_points) / (2 * (P_sum_fga + 0.44 * P_sum_fta))

# Round the PLY Stats
P_avg_pts = round(P_avg_pts, 1)
P_avg_ast = round(P_avg_ast, 1)
P_avg_reb = round(P_avg_reb, 1)
P_avg_steals = round(P_avg_steals, 1)
P_avg_blocks = round(P_avg_blocks, 1)
P_avg_fg = round(P_avg_fg, 3)
P_avg_efg = round(P_avg_efg, 3)
P_avg_ts = round(P_avg_ts, 3)

print("PLY Career Avg Points: ", P_avg_pts)
print("PLY Career Avg Assists: ", P_avg_ast)
print("PLY Career Avg Rebounds: ", P_avg_reb)
print("PLY Career Avg Steals: ", P_avg_steals)
print("PLY Career Avg Blocks: ", P_avg_blocks)
print("PLY Career Field Goal %: ", P_avg_fg)
print("PLY Career e-Field Goal %: ", P_avg_efg)
print("PLY Career True Shooting %: ", P_avg_ts)

C_avg_pts = (R_avg_pts + P_avg_pts) / 2
C_avg_ast = (R_avg_ast + P_avg_ast) / 2
C_avg_reb = (R_avg_reb + P_avg_reb) / 2
C_avg_steals = (R_avg_steals + P_avg_steals) / 2
C_avg_blocks = (R_avg_blocks + P_avg_blocks) / 2
C_avg_fg = (R_avg_fg + P_avg_fg) / 2
C_avg_efg = (R_avg_efg + P_avg_efg) / 2
C_avg_ts = (R_avg_ts + P_avg_ts) / 2

# Round the CMB Stats
C_avg_pts = round(C_avg_pts, 1)
C_avg_ast = round(C_avg_ast, 1)
C_avg_reb = round(C_avg_reb, 1)
C_avg_steals = round(C_avg_steals, 1)
C_avg_blocks = round(C_avg_blocks, 1)
C_avg_fg = round(C_avg_fg, 3)
C_avg_efg = round(C_avg_efg, 3)
C_avg_ts = round(C_avg_ts, 3)

print("CMB Career Avg Points: ", C_avg_pts)
print("CMB Career Avg Assists: ", C_avg_ast)
print("CMB Career Avg Rebounds: ", C_avg_reb)
print("CMB Career Avg Steals: ", C_avg_steals)
print("CMB Career Avg Blocks: ", C_avg_blocks)
print("CMB Career Field Goal %: ", C_avg_fg)
print("CMB Career e-Field Goal %: ", C_avg_efg)
print("CMB Career True Shooting %: ", C_avg_ts)