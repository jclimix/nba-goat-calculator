from nba_api.stats.static import teams
from nba_api.stats.endpoints import commonteamroster

rows = 75
cols = 75
champ_array = [[0 for _ in range(cols)] for _ in range(rows)]

champ_array[0][0] = '1610612747'
champ_array[0][1] = '1610612758'
champ_array[0][2] = '1610612747'
champ_array[0][3] = '1610612747'
champ_array[0][4] = '1610612747'
champ_array[0][5] = '1610612755'
champ_array[0][6] = '1610612744'
champ_array[0][7] = '1610612738'
champ_array[0][8] = '1610612737'
champ_array[0][9] = '1610612738'
champ_array[0][10] = '1610612738'
champ_array[0][11] = '1610612738'
champ_array[0][12] = '1610612738'
champ_array[0][13] = '1610612738'
champ_array[0][14] = '1610612738'
champ_array[0][15] = '1610612738'
champ_array[0][16] = '1610612738'
champ_array[0][17] = '1610612755'
champ_array[0][18] = '1610612738'
champ_array[0][19] = '1610612738'
champ_array[0][20] = '1610612752'
champ_array[0][21] = '1610612749'
champ_array[0][22] = '1610612747'
champ_array[0][23] = '1610612752'
champ_array[0][24] = '1610612738'
champ_array[0][25] = '1610612744'
champ_array[0][26] = '1610612738'
champ_array[0][27] = '1610612757'
champ_array[0][28] = '1610612764'
champ_array[0][29] = '1610612760'
champ_array[0][30] = '1610612747'
champ_array[0][31] = '1610612738'
champ_array[0][32] = '1610612747'
champ_array[0][33] = '1610612755'
champ_array[0][34] = '1610612738'
champ_array[0][35] = '1610612747'
champ_array[0][36] = '1610612738'
champ_array[0][37] = '1610612747'
champ_array[0][38] = '1610612747'
champ_array[0][39] = '1610612765'
champ_array[0][40] = '1610612765'
champ_array[0][41] = '1610612741'
champ_array[0][42] = '1610612741'
champ_array[0][43] = '1610612741'
champ_array[0][44] = '1610612745'
champ_array[0][45] = '1610612745'
champ_array[0][46] = '1610612741'
champ_array[0][47] = '1610612741'
champ_array[0][48] = '1610612741'
champ_array[0][49] = '1610612759'
champ_array[0][50] = '1610612747'
champ_array[0][51] = '1610612747'
champ_array[0][52] = '1610612747'
champ_array[0][53] = '1610612759'
champ_array[0][54] = '1610612765'
champ_array[0][55] = '1610612759'
champ_array[0][56] = '1610612748'
champ_array[0][57] = '1610612759'
champ_array[0][58] = '1610612738'
champ_array[0][59] = '1610612747'
champ_array[0][60] = '1610612747'
champ_array[0][61] = '1610612742'
champ_array[0][62] = '1610612748'
champ_array[0][63] = '1610612748'
champ_array[0][64] = '1610612759'
champ_array[0][65] = '1610612744'
champ_array[0][66] = '1610612739'
champ_array[0][67] = '1610612744'
champ_array[0][68] = '1610612744'
champ_array[0][69] = '1610612761'
champ_array[0][70] = '1610612747'
champ_array[0][71] = '1610612749'
champ_array[0][72] = '1610612744'
champ_array[0][73] = '1610612743'

champ_array[1][0] = '1949-50'
champ_array[1][1] = '1950-51'
champ_array[1][2] = '1951-52'
champ_array[1][3] = '1952-53'
champ_array[1][4] = '1953-54'
champ_array[1][5] = '1954-55'
champ_array[1][6] = '1955-56'
champ_array[1][7] = '1956-57'
champ_array[1][8] = '1957-58'
champ_array[1][9] = '1958-59'
champ_array[1][10] = '1959-60'
champ_array[1][11] = '1960-61'
champ_array[1][12] = '1961-62'
champ_array[1][13] = '1962-63'
champ_array[1][14] = '1963-64'
champ_array[1][15] = '1964-65'
champ_array[1][16] = '1965-66'
champ_array[1][17] = '1966-67'
champ_array[1][18] = '1967-68'
champ_array[1][19] = '1968-69'
champ_array[1][20] = '1969-70'
champ_array[1][21] = '1970-71'
champ_array[1][22] = '1971-72'
champ_array[1][23] = '1972-73'
champ_array[1][24] = '1973-74'
champ_array[1][25] = '1974-75'
champ_array[1][26] = '1975-76'
champ_array[1][27] = '1976-77'
champ_array[1][28] = '1977-78'
champ_array[1][29] = '1978-79'
champ_array[1][30] = '1979-80'
champ_array[1][31] = '1980-81'
champ_array[1][32] = '1981-82'
champ_array[1][33] = '1982-83'
champ_array[1][34] = '1983-84'
champ_array[1][35] = '1984-85'
champ_array[1][36] = '1985-86'
champ_array[1][37] = '1986-87'
champ_array[1][38] = '1987-88'
champ_array[1][39] = '1988-89'
champ_array[1][40] = '1989-90'
champ_array[1][41] = '1990-91'
champ_array[1][42] = '1991-92'
champ_array[1][43] = '1992-93'
champ_array[1][44] = '1993-94'
champ_array[1][45] = '1994-95'
champ_array[1][46] = '1995-96'
champ_array[1][47] = '1996-97'
champ_array[1][48] = '1997-98'
champ_array[1][49] = '1998-99'
champ_array[1][50] = '1999-00'
champ_array[1][51] = '2000-01'
champ_array[1][52] = '2001-02'
champ_array[1][53] = '2002-03'
champ_array[1][54] = '2003-04'
champ_array[1][55] = '2004-05'
champ_array[1][56] = '2005-06'
champ_array[1][57] = '2006-07'
champ_array[1][58] = '2007-08'
champ_array[1][59] = '2008-09'
champ_array[1][60] = '2009-10'
champ_array[1][61] = '2010-11'
champ_array[1][62] = '2011-12'
champ_array[1][63] = '2012-13'
champ_array[1][64] = '2013-14'
champ_array[1][65] = '2014-15'
champ_array[1][66] = '2015-16'
champ_array[1][67] = '2016-17'
champ_array[1][68] = '2017-18'
champ_array[1][69] = '2018-19'
champ_array[1][70] = '2019-20'
champ_array[1][71] = '2020-21'
champ_array[1][72] = '2021-22'
champ_array[1][73] = '2022-23'

i = 0
while i < rows:
    team_id = champ_array[0][i]
    season_id = champ_array[1][i]

    # Get team roster for the specified season and team
    team_roster = commonteamroster.CommonTeamRoster(team_id=team_id, season=season_id)
    team_roster_df = team_roster.get_data_frames()[0]

    all_teams = teams.get_teams()
    team_info = [team for team in all_teams if team['id'] == team_id]

    if len(team_roster_df) == 0:
        print("No roster information available for the specified season and team.")
    else:
        #team_name = team_info[0]['full_name']
        #print("Season:", season_id)
        #print("Team:", team_name)
        #print("Team ID:", team_id)

        j = 0
        while j < len(team_roster_df):
            player_name = team_roster_df.iloc[j]['PLAYER']
            player_id = team_roster_df.iloc[j]['PLAYER_ID']
            print(f"{player_id}, {player_name}, {season_id}, {team_id}")
            j = j + 1

    i = i + 1