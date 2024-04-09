from flask import Flask, render_template, request
from pprint import pprint
import pandas as pd
from tabulate import tabulate

player_count = 4815

def read_csv_as_dataframe(csv_file_path):

    try:
        df = pd.read_csv(csv_file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


csv_file_path = "jmg-nba-dataset-prod.csv"
dataframe = read_csv_as_dataframe(csv_file_path)

# Create variables for each column
index = dataframe['INDEX']
player_id = dataframe['PLAYER_ID']
player_name = dataframe['PLAYER_NAME']
r_ppg = dataframe['R_PPG']
r_apg = dataframe['R_APG']
r_rpg = dataframe['R_RPG']
r_off_reb = dataframe['R_OFF_REB']
r_def_reb = dataframe['R_DEF_REB']
r_spg = dataframe['R_SPG']
r_bpg = dataframe['R_BPG']
r_fg = dataframe['R_FG']
r_3fg = dataframe['R_3FG']
r_efg = dataframe['R_eFG']
r_ts = dataframe['R_TS']
p_ppg = dataframe['P_PPG']
p_apg = dataframe['P_APG']
p_rpg = dataframe['P_RPG']
p_off_reb = dataframe['P_OFF_REB']
p_def_reb = dataframe['P_DEF_REB']
p_spg = dataframe['P_SPG']
p_bpg = dataframe['P_BPG']
p_fg = dataframe['P_FG']
p_3fg = dataframe['P_3FG']
p_efg = dataframe['P_eFG']
p_ts = dataframe['P_TS']
reg_gw = dataframe['REG_GW']
reg_wl = dataframe['REG_WL']
ply_gw = dataframe['PLY_GW']
ply_wl = dataframe['PLY_WL']
tot_gw = dataframe['TOT_GW']
tot_gp = dataframe['TOT_GP']
tot_wl = dataframe['TOT_WL']
rings = dataframe['RINGS']
allstars = dataframe['ALLSTARS']
r_mvps = dataframe['R-MVPS']
f_mvps = dataframe['F-MVPS']
nbat1 = dataframe['NBAT1']
nbat2 = dataframe['NBAT2']
nbat3 = dataframe['NBAT3']
allstarmvps = dataframe['ALLSTARMVPS']
dpoys = dataframe['DPOYS']
rotys = dataframe['ROTYS']
smoys = dataframe['SMOYS']
mips = dataframe['MIPS']
deft1 = dataframe['DEFT1']
deft2 = dataframe['DEFT2']
rookt1 = dataframe['ROOKT1']
rookt2 = dataframe['ROOKT2']
games = dataframe['GAMES']
years = dataframe['YEARS']
season_history = dataframe['SEASONS_PLAYED']

# Convert columns to float
columns_to_convert = ['R_PPG', 'R_APG', 'R_RPG', 'R_OFF_REB', 'R_DEF_REB', 'R_SPG', 'R_BPG', 
                'R_FG', 'R_3FG', 'R_eFG', 'R_TS', 'P_PPG', 'P_APG', 'P_RPG', 'P_OFF_REB', 
                'P_DEF_REB', 'P_SPG', 'P_BPG', 'P_FG', 'P_3FG', 'P_eFG', 'P_TS', 'REG_GW', 
                'REG_WL', 'PLY_GW', 'PLY_WL', 'TOT_GW', 'TOT_GP', 'TOT_WL', 'RINGS', 
                'ALLSTARS', 'R-MVPS', 'F-MVPS', 'NBAT1', 'NBAT2', 'NBAT3', 'ALLSTARMVPS', 
                'DPOYS', 'ROTYS', 'SMOYS', 'MIPS', 'DEFT1', 'DEFT2', 'ROOKT1', 'ROOKT2', 
                'GAMES', 'YEARS']

# Convert each column to float
for col in columns_to_convert:
    dataframe[col] = dataframe[col].astype(float)

#aggregated arrays
r_score = [0] * player_count
p_score = [0] * player_count
k_score = [0] * player_count
m_score = [0] * player_count
era_score = [0] * player_count
goat_score = [0] * player_count

years50 = ["1949-50", "1950-51", "1951-52", "1952-53", "1953-54", "1954-55", "1955-56", "1956-57", "1957-58", "1958-59"]
years60 = ["1959-60", "1960-61", "1961-62", "1962-63", "1963-64", "1964-65", "1965-66", "1966-67", "1967-68", "1968-69"]
years70 = ["1969-70", "1970-71", "1971-72", "1972-73", "1973-74", "1974-75", "1975-76", "1976-77", "1977-78", "1978-79"]
years80 = ["1979-80", "1980-81", "1981-82", "1982-83", "1983-84", "1984-85", "1985-86", "1986-87", "1987-88", "1988-89"]
years90 = ["1989-90", "1990-91", "1991-92", "1992-93", "1993-94", "1994-95", "1995-96", "1996-97", "1997-98", "1998-99"]
years00 = ["1999-00", "2000-01", "2001-02", "2002-03", "2003-04", "2004-05", "2005-06", "2006-07", "2007-08", "2008-09"]
years10 = ["2009-10", "2010-11", "2011-12", "2012-13", "2013-14", "2014-15", "2015-16", "2016-17", "2017-18", "2018-19"]
years20 = ["2019-20", "2020-21", "2021-22", "2022-23"]

#define scorecard variables
inp_ppg = 0
inp_apg = 0
inp_rpg = 0
inp_orpg = 0
inp_drp = 0
inp_spg = 0
inp_bpg = 0
inp_3fg = 0
inp_fg = 0
inp_efg = 0
inp_ts = 0
inp_reg_wl = 0
inp_ply_wl = 0

inp_off_bst = 1
inp_def_bst = 1

inp_plyf_bst = 0

inp_chp_bst = 0
inp_rings = 0
inp_allstars = 0
inp_rmvp = 0
inp_fmvp = 0
inp_allstarmvp = 0
inp_dpoy = 0
inp_roty = 0
inp_smoy = 0
inp_mip = 0
inp_1T = 0
inp_2T = 0
inp_3T = 0
inp_1DT = 0
inp_2DT = 0
inp_1RT = 0
inp_2RT = 0

inp_k_bst = 1

inp_long = 0
inp_dur = 0
inp_ms_penalty = "Y"
inp_era_mode = "N"
inp_pen = 1

factor50 = 0
factor60 = 0
factor70 = 0
factor80 = 0
factor90 = 0
factor00 = 0
factor10 = 0
factor20 = 0

#input testing
print("Enter a value from 0 to 10 for the following metrics to assemble your G.O.A.T.")
inp_ppg = 7
inp_apg = 3
inp_rpg = 3
inp_orpg = 7
inp_drpg = 5
inp_spg = 4
inp_bpg = 6
inp_3fg = 10
inp_fg = 8
inp_efg = 8
inp_ts = 8
inp_reg_wl = 6
inp_ply_wl = 8
inp_off_bst = 1.1
inp_def_bst = 1.5
inp_plyf_bst = 1.5
inp_chp_bst = "Y"
inp_rings = 6
inp_allstars = 5
inp_rmvp = 5
inp_fmvp = 8
inp_allstarmvp = 5
inp_dpoy = 6
inp_roty = 4
inp_smoy = 2
inp_mip = 0
inp_1T = 7
inp_2T = 4
inp_3T = 1
inp_1DT = 7
inp_2DT = 8
inp_1RT = 4
inp_2RT = 6
inp_k_bst = 1.3
inp_long = 2
inp_dur = 2
inp_era_mode = "Y"

factor50 = 5
factor60 = 3
factor70 = 4
factor80 = 2
factor90 = 5
factor00 = 3
factor10 = 4
factor20 = 2

# Get user input from the form
inp_ppg = float(inp_ppg)
inp_apg = float(inp_apg)
inp_rpg = float(inp_rpg)
inp_orpg = float(inp_orpg)
inp_drpg = float(inp_drpg)
inp_spg = float(inp_spg)
inp_bpg = float(inp_bpg)
inp_3fg = float(inp_3fg)
inp_fg = float(inp_fg)
inp_efg = float(inp_efg)
inp_ts = float(inp_ts)
inp_reg_wl = float(inp_reg_wl)
inp_ply_wl = float(inp_ply_wl)

inp_off_bst = float(inp_off_bst)
inp_def_bst = float(inp_def_bst)
inp_plyf_bst = float(inp_plyf_bst)

inp_rings = float(inp_rings)
inp_allstars = float(inp_allstars)
inp_rmvp = float(inp_rmvp)
inp_fmvp = float(inp_fmvp)
inp_allstarmvp = float(inp_allstarmvp)
inp_dpoy = float(inp_dpoy)
inp_roty = float(inp_roty)
inp_smoy = float(inp_smoy)
inp_mip = float(inp_mip)
inp_1T = float(inp_1T)
inp_2T = float(inp_2T)
inp_3T = float(inp_3T)
inp_1DT = float(inp_1DT)
inp_2DT = float(inp_2DT)
inp_1RT = float(inp_1RT)
inp_2RT = float(inp_2RT)

inp_k_bst = float(inp_k_bst)

inp_long = float(inp_long)
inp_dur = float(inp_dur)

factor50 = float(factor50)
factor60 = float(factor60)
factor70 = float(factor70)
factor80 = float(factor80)
factor90 = float(factor90)
factor00 = float(factor00)
factor10 = float(factor10)
factor20 = float(factor20)

#ERA-Mode DISABLED
inp_era_mode = "N"
inp_orpg = 0
inp_drpg = 0

data = []

def normalize_scores(scores):

    # Find the highest and lowest scores in the list
    max_score = max(scores)
    min_score = min(scores)

    # Calculate the range of scores
    score_range = max_score - min_score

    # Convert the tuple to a list
    scores_list = list(scores)

    # Initialize an empty list for normalized scores
    normalized_scores = []

    # Divide each score by the highest score, multiply by 100, round to the nearest tenth, and append it to the normalized_scores list
    for score in scores:
        normalized_score = round(((score - min_score) / score_range) * (99.9 - 90.0) + 90.0, 1)
        normalized_scores.append(normalized_score)

    return normalized_scores

inp_ppg = float(inp_ppg)
inp_apg = float(inp_apg)
inp_rpg = float(inp_rpg)
inp_orpg = float(inp_orpg)
inp_drpg = float(inp_drpg)
inp_spg = float(inp_spg)
inp_bpg = float(inp_bpg)
inp_3fg = float(inp_3fg)
inp_fg = float(inp_fg)
inp_efg = float(inp_efg)
inp_ts = float(inp_ts)
inp_reg_wl = float(inp_reg_wl)
inp_ply_wl = float(inp_ply_wl)

inp_off_bst = float(inp_off_bst)
inp_def_bst = float(inp_def_bst)
inp_plyf_bst = float(inp_plyf_bst)

inp_rings = float(inp_rings)
inp_allstars = float(inp_allstars)
inp_rmvp = float(inp_rmvp)
inp_fmvp = float(inp_fmvp)
inp_allstarmvp = float(inp_allstarmvp)
inp_dpoy = float(inp_dpoy)
inp_roty = float(inp_roty)
inp_smoy = float(inp_smoy)
inp_mip = float(inp_mip)
inp_1T = float(inp_1T)
inp_2T = float(inp_2T)
inp_3T = float(inp_3T)
inp_1DT = float(inp_1DT)
inp_2DT = float(inp_2DT)
inp_1RT = float(inp_1RT)
inp_2RT = float(inp_2RT)

inp_k_bst = float(inp_k_bst)

inp_long = float(inp_long)
inp_dur = float(inp_dur)

factor50 = float(factor50)
factor60 = float(factor60)
factor70 = float(factor70)
factor80 = float(factor80)
factor90 = float(factor90)
factor00 = float(factor00)
factor10 = float(factor10)
factor20 = float(factor20)

inp_ppg *= 2
inp_apg *= 2
inp_rpg *= 2
inp_orpg *= 2
inp_drpg *= 2
inp_spg *= 2
inp_bpg *= 2
inp_3fg *= 2
inp_fg *= 2
inp_efg *= 2
inp_ts *= 2
inp_reg_wl *= 2
inp_ply_wl *= 2

inp_rings *= 2
inp_allstars *= 2
inp_rmvp *= 2
inp_fmvp *= 2
inp_allstarmvp *= 2
inp_dpoy *= 2
inp_roty *= 2
inp_smoy *= 2
inp_mip *= 2
inp_1T *= 2
inp_2T *= 2
inp_3T *= 2
inp_1DT *= 2
inp_2DT *= 2
inp_1RT *= 2
inp_2RT *= 2

inp_long *= 2
inp_dur *= 2


inp_chp_bst2 = 0.0

if inp_chp_bst == "Y":
    inp_chp_bst2 = 4.0
else:
    inp_chp_bst2 = 1.0

era_score = [0] * player_count

'''

for i, int_list in enumerate(season_history):  # Enumerate to get the player ID

# Look for 1950s
    found_integers = [x for x in int_list if x in years50]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor50 * 5)

# Look for 1960s
    found_integers = [x for x in int_list if x in years60]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor60 * 5)

# Look for 1970s
    found_integers = [x for x in int_list if x in years70]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor70 * 5)

# Look for 1980s
    found_integers = [x for x in int_list if x in years80]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor80 * 5)

# Look for 1990s
    found_integers = [x for x in int_list if x in years90]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor90 * 5)

# Look for 2000s
    found_integers = [x for x in int_list if x in years00]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor00 * 5)

# Look for 2010s
    found_integers = [x for x in int_list if x in years10]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor10 * 5)

# Look for 2020s
    found_integers = [x for x in int_list if x in years20]
    if found_integers:
        #print(f"Found {found_integers} in the list: {int_list}")
        era_score[i] += len(found_integers) * (factor20 * 5)

'''

#perform calculations
i = 0

#inp_era_mode = "Y"

for i in range(player_count):

        #R-Score
        r_score[i] = ((r_ppg[i] * 1 * inp_ppg * inp_off_bst) + 
        (r_apg[i] * 1.75 * inp_apg * inp_off_bst) +
        (r_rpg[i] * 1.85 * inp_rpg * ((inp_off_bst + inp_def_bst)/2)) +
        (reg_wl[i] * 10.0 * inp_reg_wl) +
        (r_spg[i] * 2.5 * inp_spg * inp_def_bst) +
        (r_bpg[i] * 1.75 * inp_bpg * inp_def_bst) +
        (r_3fg[i] * 10 * inp_3fg * inp_off_bst) +
        (r_fg[i] * 10 * inp_fg * inp_off_bst) +
        (r_efg[i] * 10 * inp_efg * inp_off_bst) +
        (r_ts[i] * 10 * inp_ts * inp_off_bst))

        #P-Score
        p_score[i] = ((p_ppg[i] * 1 * inp_ppg * inp_off_bst) + 
        (p_apg[i] * 1.75 * inp_apg * inp_off_bst) +
        (p_rpg[i] * 1.85 * inp_rpg * ((inp_off_bst + inp_def_bst)/2)) +
        (ply_wl[i] * 10 * inp_ply_wl) +
        (p_spg[i] * 2.5 * inp_spg * inp_def_bst) +
        (p_bpg[i] * 1.75 * inp_bpg * inp_def_bst) +
        (p_3fg[i] * 10 * inp_3fg * inp_off_bst) +
        (p_fg[i] * 10 * inp_fg * inp_off_bst) +
        (p_efg[i] * 10 * inp_efg * inp_off_bst) +
        (p_ts[i] * 10 * inp_ts * inp_off_bst)) * inp_plyf_bst

        #K-Score
        k_score[i] = ((inp_rings * rings[i] * 1.5 * inp_chp_bst2) +
        (allstars[i] * inp_allstars * 1.5) +
        (r_mvps[i] * inp_rmvp * 1.5) +
        (f_mvps[i] * inp_fmvp * inp_chp_bst2 * 1.5) +
        (nbat1[i] * inp_1T * 1.5) +
        (nbat2[i] * inp_2T * 1.5) +
        (nbat3[i] * inp_3T * 1.5) +
        (dpoys[i] * inp_dpoy * inp_def_bst * 1.5) +
        (rotys[i] * inp_roty * 1.5) +
        (smoys[i] * inp_smoy * 1.5) +
        (allstarmvps[i] * inp_allstarmvp * 1.5) +
        (deft1[i] * inp_1DT * inp_def_bst * 1.5) +
        (deft2[i] * inp_2DT * inp_def_bst * 1.5) +
        (rookt1[i] * inp_1RT * 1.5) +
        (rookt2[i] * inp_2RT * 1.5)) * inp_k_bst

        #M-Score
        m_score[i] = (((years[i] * 2) * inp_long) + ((games[i] / 10) * inp_dur)) / 2

        #GOAT-Score

        #Select GOAT-Score Function
        if inp_ms_penalty == "Y":
        
            goat_score[i] = (r_score[i] + p_score[i] + k_score[i] + era_score[i]) - (m_score[i] * float(inp_pen))

        if inp_ms_penalty == "N":

            goat_score[i] = (r_score[i] + p_score[i] + k_score[i] + m_score[i] + era_score[i])

        i = i + 1

ovr_score = []

ovr_score = normalize_scores(goat_score)

indexed_ovr = [(value, index) for index, value in enumerate(ovr_score)]
sorted_ovr = sorted(indexed_ovr, reverse=True)

indexed_goat = [(value, index) for index, value in enumerate(goat_score)]
sorted_goat = sorted(indexed_goat, reverse=True)

i = 1

results = 100

data = []

while i < (results + 1):
    value, index = sorted_ovr[i- 1]
    value2, index2 = sorted_goat[i- 1]
    #print(f"{i}. Name: {player_name[index]} | G-Score: {round(value, 2)}.")
    
    rank = str(i)
    name = str(player_name[index])
    os = str(round(value, 2))
    gs = str(round(value2, 2))
    rs = str(round(r_score[index], 2))
    ps = str(round(p_score[index], 2))
    ms = str(round(m_score[index], 2))
    ks = str(round(k_score[index], 2))
    es = str(round(era_score[index], 2))

    row_data = {"Player\nRank": rank, "Player\nName": name, "NBA-2K\nOVR": os, "G-Score\n(G.O.A.T. Score)": gs, "R-Score\n(Regular Season)": rs, "P-Score\n(Playoffs)": ps, "K-Score\n(Awards)": ks, "M-Score\n(Misc.)": ms, "E-Score\n(Era Score)": es}

    data.append(row_data)
    i += 1

df = pd.DataFrame(data)

table_results = tabulate(df, headers="keys", tablefmt="html", showindex=False)

inp_ppg /= 2
inp_apg /= 2                                                                                                                                                                                    
inp_rpg /= 2
inp_orpg /= 2
inp_drpg /= 2
inp_spg /= 2
inp_bpg /= 2
inp_3fg /= 2
inp_fg /= 2
inp_efg /= 2
inp_ts /= 2
inp_reg_wl /= 2
inp_ply_wl /= 2

inp_rings /= 2
inp_allstars /= 2
inp_rmvp /= 2
inp_fmvp /= 2
inp_allstarmvp /= 2
inp_dpoy /= 2
inp_roty /= 2
inp_smoy /= 2
inp_mip /= 2
inp_1T /= 2
inp_2T /= 2
inp_3T /= 2
inp_1DT /= 2
inp_2DT /= 2
inp_1RT /= 2
inp_2RT /= 2

inp_long /= 2
inp_dur /= 2


# Create a dictionary with variable names as keys and their values as values
data_scorecard = {
    'Era-Mode': [inp_era_mode],
    'PPG': [inp_ppg],
    'APG': [inp_apg],
    'RPG': [inp_rpg],
    'ORPG': [inp_orpg],
    'DRPG': [inp_drpg],
    'SPG': [inp_spg],
    'BPG': [inp_bpg],
    '3FG': [inp_3fg],
    'FG': [inp_fg],
    'EFG': [inp_efg],
    'TS': [inp_ts],
    'RegularSeason_WL': [inp_reg_wl],
    'Playoff_WL': [inp_ply_wl],
    'Playoff_Boost': [inp_plyf_bst],
    'Championship_Boost': [inp_chp_bst],
    'Champion_Boost Value': [4.0 if inp_chp_bst == "Y" else 1.0],
    'Rings': [inp_rings],
    'All_Stars': [inp_allstars],
    'RegularMVP': [inp_rmvp],
    'FinalsMVP': [inp_fmvp],
    'AllStarMVP': [inp_allstarmvp],
    'DPOY': [inp_dpoy],
    'ROTY': [inp_roty],
    '6MOY': [inp_smoy],
    'MIP': [inp_mip],
    'NBA_1st_Team': [inp_1T],
    'NBA_2nd_Team': [inp_2T],
    'NBA_3rd_Team': [inp_3T],
    '1st_Defense_Team': [inp_1DT],
    '2nd_Defense_Team': [inp_2DT],
    '1st_Rookie_Team': [inp_1RT],
    '2nd_Rookie_Team': [inp_2RT],
    'Longevity': [inp_long],
    'Durability': [inp_dur],
    'M-Score Penalty?': [inp_ms_penalty],
    'M-Score Penalty Value': [inp_pen],
    '1950s': [factor50], 
    '1960s': [factor60], 
    '1970s': [factor70], 
    '1980s': [factor80], 
    '1990s': [factor90], 
    '2000s': [factor00], 
    '2010s': [factor10], 
    '2020s': [factor20]
}

# Create a DataFrame from the dictionary
df2 = pd.DataFrame(data_scorecard)

transposed_df2 = df2.transpose()

print(df)