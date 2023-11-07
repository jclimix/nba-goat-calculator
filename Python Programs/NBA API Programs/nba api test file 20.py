from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

size = 74
champ_array = [0] * size

champ_array[0] = '1610612747'
champ_array[1] = '1610612758'
champ_array[2] = '1610612747'
champ_array[3] = '1610612747'
champ_array[4] = '1610612747'
champ_array[5] = '1610612755'
champ_array[6] = '1610612744'
champ_array[7] = '1610612738'
champ_array[8] = '1610612737'
champ_array[9] = '1610612738'
champ_array[10] = '1610612738'
champ_array[11] = '1610612738'
champ_array[12] = '1610612738'
champ_array[13] = '1610612738'
champ_array[14] = '1610612738'
champ_array[15] = '1610612738'
champ_array[16] = '1610612738'
champ_array[17] = '1610612755'
champ_array[18] = '1610612738'
champ_array[19] = '1610612738'
champ_array[20] = '1610612752'
champ_array[21] = '1610612749'
champ_array[22] = '1610612747'
champ_array[23] = '1610612752'
champ_array[24] = '1610612738'
champ_array[25] = '1610612744'
champ_array[26] = '1610612738'
champ_array[27] = '1610612757'
champ_array[28] = '1610612764'
champ_array[29] = '1610612760'
champ_array[30] = '1610612747'
champ_array[31] = '1610612738'
champ_array[32] = '1610612747'
champ_array[33] = '1610612755'
champ_array[34] = '1610612738'
champ_array[35] = '1610612747'
champ_array[36] = '1610612738'
champ_array[37] = '1610612747'
champ_array[38] = '1610612747'
champ_array[39] = '1610612765'
champ_array[40] = '1610612765'
champ_array[41] = '1610612741'
champ_array[42] = '1610612741'
champ_array[43] = '1610612741'
champ_array[44] = '1610612745'
champ_array[45] = '1610612745'
champ_array[46] = '1610612741'
champ_array[47] = '1610612741'
champ_array[48] = '1610612741'
champ_array[49] = '1610612759'
champ_array[50] = '1610612747'
champ_array[51] = '1610612747'
champ_array[52] = '1610612747'
champ_array[53] = '1610612759'
champ_array[54] = '1610612765'
champ_array[55] = '1610612759'
champ_array[56] = '1610612748'
champ_array[57] = '1610612759'
champ_array[58] = '1610612738'
champ_array[59] = '1610612747'
champ_array[60] = '1610612747'
champ_array[61] = '1610612742'
champ_array[62] = '1610612748'
champ_array[63] = '1610612748'
champ_array[64] = '1610612759'
champ_array[65] = '1610612744'
champ_array[66] = '1610612739'
champ_array[67] = '1610612744'
champ_array[68] = '1610612744'
champ_array[69] = '1610612761'
champ_array[70] = '1610612747'
champ_array[71] = '1610612749'
champ_array[72] = '1610612744'
champ_array[73] = '1610612743'

sea_1 = 1949
sea_2 = 50

i = 0
while i < size:

    season_str = f"{sea_1}-{sea_2}"
    season_id = season_str
    team_nickname = champ_array[i]

    # Get team roster for the specified season and team
    team_roster = commonteamroster.CommonTeamRoster(team_id=champ_array[i], season=season_id)
    team_roster_df = team_roster.get_data_frames()[0]

    all_teams = teams.get_teams()
    team_info = [team for team in all_teams if team['id'] == champ_array[i]]

    if len(team_roster_df) == 0:
        print("No roster information available for the specified season and team.")
    else:
        #team_name = team_info[0]['full_name']
        print("Season:", season_id)
        #print("Team:", team_name)
        print("Team ID:", champ_array[i])

        j = 0
        while j < len(team_roster_df):
            player_name = team_roster_df.iloc[j]['PLAYER']
            player_id = team_roster_df.iloc[j]['PLAYER_ID']
            print(f"{player_id}, {player_name}, {season_id}")
            j = j + 1

    i = i + 1
    sea_1 = sea_1 + 1
    sea_2 = sea_2 + 1