from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats

# Get a list of all players
all_players = players.get_players()

# Display the Column Headers
print("PLAYER_ID, PLAYER_NAME, PPG, APG, RPG, SPG, BPG, FG, eFG, TS")

# Iterate through each player and fetch their career stats
for player in all_players:
    player_name = player['full_name']
    player_id = player['id']
    
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
    career_stats_df = career_stats.get_data_frames()[1]
    
    if len(career_stats_df) > 0:
        REG_total_points = career_stats_df.iloc[0]['PTS']
        REG_total_rebounds = career_stats_df.iloc[0]['REB']
        REG_total_assists = career_stats_df.iloc[0]['AST']
        REG_total_steals = career_stats_df.iloc[0]['STL']
        REG_total_blocks = career_stats_df.iloc[0]['BLK']
        REG_total_turnovers = career_stats_df.iloc[0]['TOV']
        REG_total_fgm = career_stats_df.iloc[0]['FGM']
        REG_total_3pm = career_stats_df.iloc[0]['FG3M']
        REG_total_fga = career_stats_df.iloc[0]['FGA']
        REG_total_fta = career_stats_df.iloc[0]['FTA']
        REG_total_ftm = career_stats_df.iloc[0]['FTM']
        REG_total_gp = career_stats_df.iloc[0]['GP']
        
        #points
        REG_PPG = REG_total_points / REG_total_gp

        #asssts
        REG_APG = REG_total_assists / REG_total_gp

        #rebounds
        if REG_total_rebounds != None:
            REG_RPG = REG_total_rebounds / REG_total_gp
        else:
            REG_RPG = 0

        #steals
        if REG_total_steals != None:
            REG_SPG = REG_total_steals / REG_total_gp
        else:
            REG_SPG = 0

        #blocks
        if REG_total_blocks != None:
            REG_BPG = REG_total_blocks / REG_total_gp
        else:
            REG_BPG = 0

        #field goal pct
        REG_FG = REG_total_fgm / REG_total_fga

        #effective field goal pct
        if REG_total_3pm != None:
            REG_EFG = (REG_total_fgm + 0.5 * float(REG_total_3pm)) / REG_total_fga
        else:
            REG_EFG = 0

        #true shooting
        REG_TS = (REG_total_points) / (2 * (REG_total_fga + 0.44 * REG_total_fta))

        print(player_id, ",", player_name, ",", REG_PPG, ",", REG_APG, ",", REG_RPG, ",", REG_SPG, ",", REG_BPG, ",", REG_FG, ",", REG_EFG, ",", REG_TS)
