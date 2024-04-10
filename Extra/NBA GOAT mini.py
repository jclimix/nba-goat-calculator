#from dotenv import load_dotenv
from pprint import pprint
import os
import pandas as pd
from tabulate import tabulate

def find_goat():

    #Init empty DataFrame
    columns = ["Rank","Name", "G-Score", "R-Score", "P-Score", "M-Score", "K-Score"]
    df = pd.DataFrame(columns=columns)

    player_count = 4816

    #define scorecard variables
    inp_ppg = 0
    inp_apg = 0
    inp_rpg = 0
    inp_spg = 0
    inp_bpg = 0
    inp_3fg = 0
    inp_fg = 0
    inp_efg = 0
    inp_ts = 0
    inp_plyf_bst = 0
    inp_chp_bst = 0
    inp_rings = 0
    inp_allstars = 0
    inp_rmvp = 0
    inp_fmvp = 0
    inp_1T = 0
    inp_2T = 0
    inp_3T = 0
    inp_long = 0
    inp_dur = 0
    inp_ms_penalty = "Y"
    inp_pen = 1

    ##user input
    #print("Enter a value from 0 to 10 for the following metrics to assemble your G.O.A.T.")
    #inp_ppg = input("Points Per Game: ")
    #inp_apg = input("Assists Per Game: ")
    #inp_rpg = input("Rebounds Per Game: ")
    #inp_spg = input("Steals Per Game: ")
    #inp_bpg = input("Blocks Per Game: ")
    #inp_3fg = input("3-Point Field Goal Percentage: ")
    #inp_fg = input("Field Goal Percentage: ")
    #inp_efg = input("Effective Field Goal Percentage: ")
    #inp_ts = input("True Shooting Percentage: ")
    #inp_plyf_bst = input("Playoff BOOST (1.1, 1.25, 1.5): ")
    #inp_chp_bst = input("Championship BOOST (Y or N): ")
    #inp_rings = input("Championships: ")
    #inp_allstars = input("All-Star Appearances: ")
    #inp_rmvp = input("Regular Season MVPs: ")
    #inp_fmvp = input("Finals MVPs: ")
    #inp_1T = input("All-NBA First Teams: ")
    #inp_2T = input("All-NBA Second Teams: ")
    #inp_3T = input("All-NBA Third Teams: ")
    #inp_long = input("Longevity: ")
    #inp_dur = input("Durability: ")
    #inp_ms_penalty = input("Do you want to implement a penalty based on the M-Score?\nNOTE:Selecting 'Yes' will reward players that have played less in the NBA while penalizing players with longer careers and more games played.")
    if inp_ms_penalty == "Y" or "y":
        inp_pen = input("Enter a value from 0 to 5 to determine the weight of the penalty. A higher value will result in a larger penalty: ")

    #input testing
    print("Enter a value from 0 to 10 for the following metrics to assemble your G.O.A.T.")
    inp_ppg = 7
    inp_apg = 3
    inp_rpg = 3
    inp_spg = 4
    inp_bpg = 6
    inp_3fg = 10
    inp_fg = 8
    inp_efg = 8
    inp_ts = 8
    inp_plyf_bst = 1.5
    inp_chp_bst = "Y"
    inp_rings = 6
    inp_allstars = 5
    inp_rmvp = 5
    inp_fmvp = 8
    inp_1T = 7
    inp_2T = 4
    inp_3T = 1
    inp_long = 2
    inp_dur = 2

    inp_ppg = float(inp_ppg)
    inp_apg = float(inp_apg)
    inp_rpg = float(inp_rpg)
    inp_spg =float(inp_spg)
    inp_bpg =float(inp_bpg)
    inp_3fg =float(inp_3fg)
    inp_fg =float(inp_fg)
    inp_efg =float(inp_efg)
    inp_ts =float(inp_ts)
    inp_plyf_bst = float(inp_plyf_bst)

    inp_rings =float(inp_rings)
    inp_allstars =float(inp_allstars)
    inp_rmvp =float(inp_rmvp)
    inp_fmvp =float(inp_fmvp)
    inp_1T =float(inp_1T)
    inp_2T =float(inp_2T)
    inp_3T =float(inp_3T)
    inp_long =float(inp_long)
    inp_dur =float(inp_dur)

    inp_chp_bst2 = 0.0

    if inp_chp_bst == "Y":
        inp_chp_bst2 = 4.0
    else:
        inp_chp_bst2 = 1.0

    #perform calculations
    i = 0

    for i in range(player_count):
        #R-Score
        r_score[i] = ((r_ppg[i] * 1 * inp_ppg) + 
        (r_apg[i] * 1.75 * inp_apg) +
        (r_rpg[i] * 1.75 * inp_rpg) +
        (r_spg[i] * 2.5 * inp_spg) +
        (r_bpg[i] * 1.75 * inp_bpg) +
        (r_3fg[i] * 10 * inp_3fg) +
        (r_fg[i] * 10 * inp_fg) +
        (r_efg[i] * 10 * inp_efg) +
        (r_ts[i] * 10 * inp_ts))

        #P-Score
        p_score[i] = ((p_ppg[i] * 1 * inp_ppg) + 
        (p_apg[i] * 1.75 * inp_apg) +
        (p_rpg[i] * 1.75 * inp_rpg) +
        (p_spg[i] * 2.5 * inp_spg) +
        (p_bpg[i] * 1.75 * inp_bpg) +
        (p_3fg[i] * 10 * inp_3fg) +
        (p_fg[i] * 10 * inp_fg) +
        (p_efg[i] * 10 * inp_efg) +
        (p_ts[i] * 10 * inp_ts)) * inp_plyf_bst

        #K-Score
        k_score[i] = ((inp_rings * rings[i] * inp_chp_bst2) +
        (all_stars[i] * inp_allstars) +
        (r_mvp[i] * inp_rmvp) +
        (f_mvp[i] * inp_fmvp * inp_chp_bst2) +
        (first_team[i] * inp_1T) +
        (second_team[i] * inp_2T) +
        (third_team[i] * inp_3T))

        #M-Score
        m_score[i] = (((years[i] * 4) * inp_long) +
        ((games[i] / 20) * inp_dur)) / 5

        #GOAT-Score

        #Select GOAT-Score Function
        if inp_ms_penalty == "Y" or "y":
        
            goat_score[i] = (r_score[i] + p_score[i] + k_score[i]) - (m_score[i] * float(inp_pen))

        else:

            goat_score[i] = r_score[i] + p_score[i] + k_score[i] + m_score[i]

        i = i + 1

    indexed_goat = [(value, index) for index, value in enumerate(goat_score)]
    sorted_goat = sorted(indexed_goat, reverse=True)

    i = 1

    results = 50

    data = []

    while i < (results + 1):
        value, index = sorted_goat[i- 1]
        #print(f"{i}. Name: {player_name[index]} | G-Score: {round(value, 2)}.")
        
        rank = str(i)
        name = str(player_name[index])
        gs = str(round(value, 2))
        rs = str(round(r_score[index], 2))
        ps = str(round(p_score[index], 2))
        ms = str(round(m_score[index], 2))
        ks = str(round(k_score[index], 2))

        row_data = {"Rank": rank, "Name": name, "G-Score": gs, "R-Score": rs, "P-Score": ps, "M-Score": ms, "K-Score": ks}

        data.append(row_data)
        i += 1

    df = pd.DataFrame(data)

    table = tabulate(df, headers="keys", tablefmt="pretty", showindex=False)
    
    return table

if __name__ == "__main__":
    print('\n***Find User GOAT ***\n')