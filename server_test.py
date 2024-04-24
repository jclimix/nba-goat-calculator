from app.calc import Calculator

from flask import Flask, render_template, request
import pandas as pd
from tabulate import tabulate
from waitress import serve


app = Flask(__name__)

test = "Y"

test_cases = {
    'inp_ppg': '7',
    'inp_apg': '5',
    'inp_rpg': '9',
    'inp_spg': '3',
    'inp_bpg': '2',
    'inp_3fg': '8',
    'inp_fg': '8',
    'inp_efg': '7',
    'inp_ts': '9',
    'inp_reg_wl': '6',
    'inp_ply_wl': '5',
    'inp_off_bst': '7',
    'inp_def_bst': '6',
    'inp_plyf_bst': '8',
    'inp_chp_bst': 'Y',
    'inp_rings': '5',
    'inp_allstars': '8',
    'inp_rmvp': '4',
    'inp_fmvp': '3',
    'inp_allstarmvp': '6',
    'inp_dpoy': '7',
    'inp_roty': '5',
    'inp_smoy': '4',
    'inp_mip': '5',
    'inp_1T': '6',
    'inp_2T': '5',
    'inp_3T': '4',
    'inp_1DT': '7',
    'inp_2DT': '6',
    'inp_1RT': '5',
    'inp_2RT': '4',
    'inp_k_bst': '8',
    'inp_long': '7',
    'inp_dur': '6',
    'inp_ms_penalty': 'Y',
    'inp_pen': '3',
    'inp_score_mode': 'S'
}

calc = Calculator()


@app.route('/', methods=['GET', 'POST'])
def find_goat_web():
    if request.method == 'POST':

        if test == "Y":

            form_data = test_cases

            inp_points_pergame = float(form_data['inp_ppg'])
            inp_assists_pergame = float(form_data['inp_apg'])
            inp_rebounds_pergame = float(form_data['inp_rpg'])
            inp_steals_pergame = float(form_data['inp_spg'])
            inp_blocks_pergame = float(form_data['inp_bpg'])
            inp_three_pt_fieldgoal_pct = float(form_data['inp_3fg'])
            inp_fieldgoal_pct = float(form_data['inp_fg'])
            inp_effective_fieldgoal_pct = float(form_data['inp_efg'])
            inp_true_shooting_pct = float(form_data['inp_ts'])
            inp_regular_szn_win_pct = float(form_data['inp_reg_wl'])
            inp_playoffs_win_pct = float(form_data['inp_ply_wl'])

            inp_offensive_boost = float(form_data['inp_off_bst'])
            inp_defensive_boost = float(form_data['inp_def_bst'])
            inp_playoffs_boost = float(form_data['inp_plyf_bst'])
            inp_championship_boost_YN = form_data['inp_chp_bst']

            inp_championships = float(form_data['inp_rings'])
            inp_allstar_selections = float(form_data['inp_allstars'])
            inp_regular_szn_mvps = float(form_data['inp_rmvp'])
            inp_finals_mvps = float(form_data['inp_fmvp'])
            inp_allstar_mvps = float(form_data['inp_allstarmvp'])
            inp_defensivePlayerOfTheYear = float(form_data['inp_dpoy'])
            inp_rookieOfTheYear = float(form_data['inp_roty'])
            inp_sixthManOfTheYear = float(form_data['inp_smoy'])
            inp_mostImprovedPlayer = float(form_data['inp_mip'])
            inp_all_NBA_1stTeam = float(form_data['inp_1T'])
            inp_all_NBA_2ndTeam = float(form_data['inp_2T'])
            inp_all_NBA_3rdTeam = float(form_data['inp_3T'])
            inp_all_NBA_defensive_1stTeam = float(form_data['inp_1DT'])
            inp_all_NBA_defensive_2ndTeam = float(form_data['inp_2DT'])
            inp_all_NBA_rookie_1stTeam = float(form_data['inp_1RT'])
            inp_all_NBA_rookie_2ndTeam = float(form_data['inp_2RT'])

            inp_kudos_score_boost = float(form_data['inp_k_bst'])

            inp_longevity = float(form_data['inp_long'])
            inp_durability = float(form_data['inp_dur'])
            inp_mScore_penalty_YN = form_data['inp_ms_penalty']
            inp_mScore_penalty = float(form_data['inp_pen'])

            inp_score_mode = form_data['inp_score_mode']

        csv_file_path = "jmg_nba_dataset_prod.csv"
        dataframe: pd.DataFrame = calc.read_csv_as_dataframe(csv_file_path)

        players = calc.create_players_from_dataframe(dataframe)

        if players is not None:
            player_count = len(dataframe.index)
        else:
            player_count = 0

        if dataframe is None:
            print("Nothing here...")

        # Create variables for each column
        idx = dataframe.INDEX
        player_id = dataframe['PLAYER_ID']
        player_name = dataframe['PLAYER_NAME']
        reg_szn_points_pergame = dataframe['R_PPG']
        reg_szn_assists_pergame = dataframe['R_APG']
        reg_szn_rebounds_pergame = dataframe['R_RPG']
        reg_szn_steals_pergame = dataframe['R_SPG']
        reg_szn_blocks_pergame = dataframe['R_BPG']
        reg_szn_fieldgoal_pct = dataframe['R_FG']
        reg_szn_three_pt_fieldgoal_pct = dataframe['R_3FG']
        reg_szn_effective_fieldgoal_pct = dataframe['R_eFG']
        reg_szn_true_shooting_pct = dataframe['R_TS']
        playoffs_points_pergame = dataframe['P_PPG']
        playoffs_assists_pergame = dataframe['P_APG']
        playoffs_rebounds_pergame = dataframe['P_RPG']
        playoffs_steals_pergame = dataframe['P_SPG']
        playoffs_blocks_pergame = dataframe['P_BPG']
        playoffs_fieldgoal_pct = dataframe['P_FG']
        playoffs_three_pt_fieldgoal_pct = dataframe['P_3FG']
        playoffs_effective_fieldgoal_pct = dataframe['P_eFG']
        playoffs_true_shooting_pct = dataframe['P_TS']
        regular_szn_win_pct = dataframe['REG_WL']
        playoffs_win_pct = dataframe['PLY_WL']
        rings = dataframe['RINGS']
        allstars = dataframe['ALLSTARS']
        reg_szn_mvps = dataframe['R-MVPS']
        finals_mvps = dataframe['F-MVPS']
        all_NBA_1stTeam = dataframe['NBAT1']
        all_NBA_2ndTeam = dataframe['NBAT2']
        all_NBA_3rdTeam = dataframe['NBAT3']
        allstar_mvps = dataframe['ALLSTARMVPS']
        defensivePlayerOfTheYear = dataframe['DPOYS']
        rookieOfTheYears = dataframe['ROTYS']
        sixthManOfTheYears = dataframe['SMOYS']
        mostImprovedPlayer = dataframe['MIPS']
        all_NBA_defensive_1stTeam = dataframe['DEFT1']
        all_NBA_defensive_2ndTeam = dataframe['DEFT2']
        all_NBA_rookie_1stTeam = dataframe['ROOKT1']
        all_NBA_rookie_2ndTeam = dataframe['ROOKT2']
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

        # aggregated arrays
        reg_szn_score = [0] * player_count
        playoffs_score = [0] * player_count
        kudos_score = [0] * player_count
        misc_score = [0] * player_count
        goat_score = [0] * player_count

        # Get user input from the form
        inp_points_pergame = float(request.form['inp_ppg'])
        inp_assists_pergame = float(request.form['inp_apg'])
        inp_rebounds_pergame = float(request.form['inp_rpg'])
        inp_steals_pergame = float(request.form['inp_spg'])
        inp_blocks_pergame = float(request.form['inp_bpg'])
        inp_three_pt_fieldgoal_pct = float(request.form['inp_3fg'])
        inp_fieldgoal_pct = float(request.form['inp_fg'])
        inp_effective_fieldgoal_pct = float(request.form['inp_efg'])
        inp_true_shooting_pct = float(request.form['inp_ts'])
        inp_regular_szn_win_pct = float(request.form['inp_reg_wl'])
        inp_playoffs_win_pct = float(request.form['inp_ply_wl'])

        inp_offensive_boost = float(request.form['inp_off_bst'])
        inp_defensive_boost = float(request.form['inp_def_bst'])
        inp_playoffs_boost = float(request.form['inp_plyf_bst'])
        inp_championship_boost_YN = request.form['inp_chp_bst']

        inp_championships = float(request.form['inp_rings'])
        inp_allstar_selections = float(request.form['inp_allstars'])
        inp_regular_szn_mvps = float(request.form['inp_rmvp'])
        inp_finals_mvps = float(request.form['inp_fmvp'])
        inp_allstar_mvps = float(request.form['inp_allstarmvp'])
        inp_defensivePlayerOfTheYear = float(request.form['inp_dpoy'])
        inp_rookieOfTheYear = float(request.form['inp_roty'])
        inp_sixthManOfTheYear = float(request.form['inp_smoy'])
        inp_mostImprovedPlayer = float(request.form['inp_mip'])
        inp_all_NBA_1stTeam = float(request.form['inp_1T'])
        inp_all_NBA_2ndTeam = float(request.form['inp_2T'])
        inp_all_NBA_3rdTeam = float(request.form['inp_3T'])
        inp_all_NBA_defensive_1stTeam = float(request.form['inp_1DT'])
        inp_all_NBA_defensive_2ndTeam = float(request.form['inp_2DT'])
        inp_all_NBA_rookie_1stTeam = float(request.form['inp_1RT'])
        inp_all_NBA_rookie_2ndTeam = float(request.form['inp_2RT'])

        inp_kudos_score_boost = float(request.form['inp_k_bst'])

        inp_longevity = float(request.form['inp_long'])
        inp_durability = float(request.form['inp_dur'])
        inp_mScore_penalty_YN = (request.form['inp_ms_penalty'])
        inp_mScore_penalty = float(request.form['inp_pen'])

        inp_score_mode = request.form['inp_score_mode']

        # inp_score_mode = "S"
        inp_points_pergame = float(request.form['inp_ppg'])
        inp_assists_pergame = float(request.form['inp_apg'])
        inp_rebounds_pergame = float(request.form['inp_rpg'])
        inp_steals_pergame = float(request.form['inp_spg'])
        inp_blocks_pergame = float(request.form['inp_bpg'])
        inp_three_pt_fieldgoal_pct = float(request.form['inp_3fg'])
        inp_fieldgoal_pct = float(request.form['inp_fg'])
        inp_effective_fieldgoal_pct = float(request.form['inp_efg'])
        inp_true_shooting_pct = float(request.form['inp_ts'])
        inp_regular_szn_win_pct = float(request.form['inp_reg_wl'])
        inp_playoffs_win_pct = float(request.form['inp_ply_wl'])

        inp_offensive_boost = float(request.form['inp_off_bst'])
        inp_defensive_boost = float(request.form['inp_def_bst'])
        inp_playoffs_boost = float(request.form['inp_plyf_bst'])
        inp_championship_boost_YN = request.form['inp_chp_bst']

        inp_championships = float(request.form['inp_rings'])
        inp_allstar_selections = float(request.form['inp_allstars'])
        inp_regular_szn_mvps = float(request.form['inp_rmvp'])
        inp_finals_mvps = float(request.form['inp_fmvp'])
        inp_allstar_mvps = float(request.form['inp_allstarmvp'])
        inp_defensivePlayerOfTheYear = float(request.form['inp_dpoy'])
        inp_rookieOfTheYear = float(request.form['inp_roty'])
        inp_sixthManOfTheYear = float(request.form['inp_smoy'])
        inp_mostImprovedPlayer = float(request.form['inp_mip'])
        inp_all_NBA_1stTeam = float(request.form['inp_1T'])
        inp_all_NBA_2ndTeam = float(request.form['inp_2T'])
        inp_all_NBA_3rdTeam = float(request.form['inp_3T'])
        inp_all_NBA_defensive_1stTeam = float(request.form['inp_1DT'])
        inp_all_NBA_defensive_2ndTeam = float(request.form['inp_2DT'])
        inp_all_NBA_rookie_1stTeam = float(request.form['inp_1RT'])
        inp_all_NBA_rookie_2ndTeam = float(request.form['inp_2RT'])

        inp_kudos_score_boost = float(request.form['inp_k_bst'])

        inp_longevity = float(request.form['inp_long'])
        inp_durability = float(request.form['inp_dur'])
        inp_mScore_penalty_YN = (request.form['inp_ms_penalty'])
        inp_mScore_penalty = float(request.form['inp_pen'])

        inp_score_mode = request.form['inp_score_mode']

        # inp_score_mode = "S"

        data = []

        def normalize_scores(scores):

            # Find the highest and lowest scores in the list
            max_score = max(scores)
            min_score = min(scores)

            # Calculate the range of scores
            score_range = max_score - min_score

            # Initialize an empty list for normalized scores
            normalized_scores = []

            # Divide each score by the highest score, multiply by 100, round to the nearest tenth, and append it to the normalized_scores list
            for score in scores:
                normalized_score = round(
                    ((score - min_score) / score_range) * (99.9 - 90.0) + 90.0, 1)
                normalized_scores.append(normalized_score)

            return normalized_scores

        inp_points_pergame = float(inp_points_pergame)
        inp_assists_pergame = float(inp_assists_pergame)
        inp_rebounds_pergame = float(inp_rebounds_pergame)
        inp_steals_pergame = float(inp_steals_pergame)
        inp_blocks_pergame = float(inp_blocks_pergame)
        inp_three_pt_fieldgoal_pct = float(inp_three_pt_fieldgoal_pct)
        inp_fieldgoal_pct = float(inp_fieldgoal_pct)
        inp_effective_fieldgoal_pct = float(inp_effective_fieldgoal_pct)
        inp_true_shooting_pct = float(inp_true_shooting_pct)
        inp_regular_szn_win_pct = float(inp_regular_szn_win_pct)
        inp_playoffs_win_pct = float(inp_playoffs_win_pct)

        inp_offensive_boost = float(inp_offensive_boost)
        inp_defensive_boost = float(inp_defensive_boost)
        inp_playoffs_boost = float(inp_playoffs_boost)

        inp_championships = float(inp_championships)
        inp_allstar_selections = float(inp_allstar_selections)
        inp_regular_szn_mvps = float(inp_regular_szn_mvps)
        inp_finals_mvps = float(inp_finals_mvps)
        inp_allstar_mvps = float(inp_allstar_mvps)
        inp_defensivePlayerOfTheYear = float(inp_defensivePlayerOfTheYear)
        inp_rookieOfTheYear = float(inp_rookieOfTheYear)
        inp_sixthManOfTheYear = float(inp_sixthManOfTheYear)
        inp_mostImprovedPlayer = float(inp_mostImprovedPlayer)
        inp_all_NBA_1stTeam = float(inp_all_NBA_1stTeam)
        inp_all_NBA_2ndTeam = float(inp_all_NBA_2ndTeam)
        inp_all_NBA_3rdTeam = float(inp_all_NBA_3rdTeam)
        inp_all_NBA_defensive_1stTeam = float(inp_all_NBA_defensive_1stTeam)
        inp_all_NBA_defensive_2ndTeam = float(inp_all_NBA_defensive_2ndTeam)
        inp_all_NBA_rookie_1stTeam = float(inp_all_NBA_rookie_1stTeam)
        inp_all_NBA_rookie_2ndTeam = float(inp_all_NBA_rookie_2ndTeam)

        inp_kudos_score_boost = float(inp_kudos_score_boost)

        inp_longevity = float(inp_longevity)
        inp_durability = float(inp_durability)

        inp_points_pergame *= 2
        inp_assists_pergame *= 2
        inp_rebounds_pergame *= 2
        inp_steals_pergame *= 2
        inp_blocks_pergame *= 2
        inp_three_pt_fieldgoal_pct *= 2
        inp_fieldgoal_pct *= 2
        inp_effective_fieldgoal_pct *= 2
        inp_true_shooting_pct *= 2
        inp_regular_szn_win_pct *= 2
        inp_playoffs_win_pct *= 2

        inp_championships *= 2
        inp_allstar_selections *= 2
        inp_regular_szn_mvps *= 2
        inp_finals_mvps *= 2
        inp_allstar_mvps *= 2
        inp_defensivePlayerOfTheYear *= 2
        inp_rookieOfTheYear *= 2
        inp_sixthManOfTheYear *= 2
        inp_mostImprovedPlayer *= 2
        inp_all_NBA_1stTeam *= 2
        inp_all_NBA_2ndTeam *= 2
        inp_all_NBA_3rdTeam *= 2
        inp_all_NBA_defensive_1stTeam *= 2
        inp_all_NBA_defensive_2ndTeam *= 2
        inp_all_NBA_rookie_1stTeam *= 2
        inp_all_NBA_rookie_2ndTeam *= 2

        inp_longevity *= 2
        inp_durability *= 2

        inp_championship_boost = 0.0

        if inp_championship_boost_YN == "Y":
            inp_championship_boost = 4.0
        else:
            inp_championship_boost = 1.0

        era_score = [0] * player_count

        # perform calculations

        for i in range(player_count):

            # R-Score
            print(f"{i=}")
            reg_szn_score[i] = ((reg_szn_points_pergame[i] * 1 * inp_points_pergame * inp_offensive_boost) +
                                (reg_szn_assists_pergame[i] * 1.75 * inp_assists_pergame * inp_offensive_boost) +
                                (reg_szn_rebounds_pergame[i] * 1.85 * inp_rebounds_pergame * ((inp_offensive_boost + inp_defensive_boost)/2)) +
                                (regular_szn_win_pct[i] * 10 * inp_regular_szn_win_pct) +
                                (reg_szn_steals_pergame[i] * 2.5 * inp_steals_pergame * inp_defensive_boost) +
                                (reg_szn_blocks_pergame[i] * 1.75 * inp_blocks_pergame * inp_defensive_boost) +
                                (reg_szn_three_pt_fieldgoal_pct[i] * 10 * inp_three_pt_fieldgoal_pct * inp_offensive_boost) +
                                (reg_szn_fieldgoal_pct[i] * 10 * inp_fieldgoal_pct * inp_offensive_boost) +
                                (reg_szn_effective_fieldgoal_pct[i] * 10 * inp_effective_fieldgoal_pct * inp_offensive_boost) +
                                (reg_szn_true_shooting_pct[i] * 10 * inp_true_shooting_pct * inp_offensive_boost))

            # P-Score
            playoffs_score[i] = ((playoffs_points_pergame[i] * 1 * inp_points_pergame * inp_offensive_boost) +
                                 (playoffs_assists_pergame[i] * 1.75 * inp_assists_pergame * inp_offensive_boost) +
                                 (playoffs_rebounds_pergame[i] * 1.85 * inp_rebounds_pergame * ((inp_offensive_boost + inp_defensive_boost)/2)) +
                                 (playoffs_win_pct[i] * 10 * inp_playoffs_win_pct) +
                                 (playoffs_steals_pergame[i] * 2.5 * inp_steals_pergame * inp_defensive_boost) +
                                 (playoffs_blocks_pergame[i] * 1.75 * inp_blocks_pergame * inp_defensive_boost) +
                                 (playoffs_three_pt_fieldgoal_pct[i] * 10 * inp_three_pt_fieldgoal_pct * inp_offensive_boost) +
                                 (playoffs_fieldgoal_pct[i] * 10 * inp_fieldgoal_pct * inp_offensive_boost) +
                                 (playoffs_effective_fieldgoal_pct[i] * 10 * inp_effective_fieldgoal_pct * inp_offensive_boost) +
                                 (playoffs_true_shooting_pct[i] * 10 * inp_true_shooting_pct * inp_offensive_boost)) * inp_playoffs_boost

            # K-Score
            kudos_score[i] = (((inp_championships * rings[i] * 1.1 * inp_championship_boost) +
                               (allstars[i] * inp_allstar_selections * 1.5) +
                               (reg_szn_mvps[i] * inp_regular_szn_mvps * 1.5) +
                               (finals_mvps[i] * inp_finals_mvps * inp_championship_boost * 1.1) +
                               (all_NBA_1stTeam[i] * inp_all_NBA_1stTeam * 1.5) +
                               (all_NBA_2ndTeam[i] * inp_all_NBA_2ndTeam * 1.5) +
                               (all_NBA_3rdTeam[i] * inp_all_NBA_3rdTeam * 1.5) +
                               (defensivePlayerOfTheYear[i] * inp_defensivePlayerOfTheYear * inp_defensive_boost * 1.5) +
                               (rookieOfTheYears[i] * inp_rookieOfTheYear * 1.5) +
                               (sixthManOfTheYears[i] * inp_sixthManOfTheYear * 1.5) +
                               (allstar_mvps[i] * inp_allstar_mvps * 1.5) +
                               (all_NBA_defensive_1stTeam[i] * inp_all_NBA_defensive_1stTeam * inp_defensive_boost * 1.5) +
                               (all_NBA_defensive_2ndTeam[i] * inp_all_NBA_defensive_2ndTeam * inp_defensive_boost * 1.5) +
                               (all_NBA_rookie_1stTeam[i] * inp_all_NBA_rookie_1stTeam * 1.5) +
                               (all_NBA_rookie_2ndTeam[i] * inp_all_NBA_rookie_2ndTeam * 1.5)) * .8) * inp_kudos_score_boost

            # M-Score
            misc_score[i] = ((((years[i] * 2) * inp_longevity) +
                             ((games[i] / 10) * inp_durability)) / 2) * 1.1

            # GOAT-Score

            # Select GOAT-Score Function
            if inp_mScore_penalty_YN == "Y":

                goat_score[i] = (reg_szn_score[i] + playoffs_score[i] + kudos_score[i] +
                                 era_score[i]) - (misc_score[i] * float(inp_mScore_penalty))

            if inp_mScore_penalty_YN == "N":

                goat_score[i] = (reg_szn_score[i] + playoffs_score[i] +
                                 kudos_score[i] + misc_score[i] + era_score[i])

            i = i + 1

        overall_score = []

        overall_score = normalize_scores(goat_score)

        indexed_ovr = [(value, index)
                       for index, value in enumerate(overall_score)]
        sorted_ovr = sorted(indexed_ovr, reverse=True)

        indexed_goat = [(value, index)
                        for index, value in enumerate(goat_score)]
        sorted_goat = sorted(indexed_goat, reverse=True)

        i = 1

        results = 100

        data = []

        def normalize_scores(scores, max_range=99.9, min_range=90.0):
            max_score = max(scores)
            min_score = min(scores)
            score_range = max_score - min_score
            normalized_scores = []

            for score in scores:
                normalized_score = round(
                    ((score - min_score) / (score_range + 1)) * (max_range - min_range) + min_range, 1)
                normalized_scores.append(normalized_score)

            return normalized_scores

        # After calculating all scores for each player...
        reg_szn_score_normalized = normalize_scores(reg_szn_score)
        playoffs_score_normalized = normalize_scores(playoffs_score)
        kudos_score_normalized = normalize_scores(kudos_score)
        misc_score_normalized = normalize_scores(misc_score)

        if inp_score_mode == "S":
            # normalize ALL scores // SIMPLE SCORING MODE
            while i < (results + 1):
                value, index = sorted_ovr[i - 1]
                value2, index2 = sorted_goat[i - 1]
                # print(f"{i}. Name: {player_name[index]} | G-Score: {round(value, 2)}.")

                rank = str(i)
                name = str(player_name[index])
                os = str(round(value, 2))
                gs = str(round(value2, 2))
                rs = str(round(reg_szn_score_normalized[index], 2))
                ps = str(round(playoffs_score_normalized[index], 2))
                ms = str(round(misc_score_normalized[index], 2))
                ks = str(round(kudos_score_normalized[index], 2))

                row_data = {"Player\nRank": rank, "Player\nName": name, "NBA-2K\nOVR": os,
                            "G-Score\n(G.O.A.T. Score)": gs, "R-Score\n(Regular Season)": rs, "P-Score\n(Playoffs)": ps, "K-Score\n(Awards)": ks, "M-Score\n(Misc.)": ms}

                data.append(row_data)
                i += 1

        if inp_score_mode == "A":
            # print raw scores // ADVANCED SCORING MODE
            while i < (results + 1):
                value, index = sorted_ovr[i - 1]
                value2, index2 = sorted_goat[i - 1]
                # print(f"{i}. Name: {player_name[index]} | G-Score: {round(value, 2)}.")

                rank = str(i)
                name = str(player_name[index])
                os = str(round(value, 2))
                gs = str(round(value2, 2))
                rs = str(round(reg_szn_score[index], 2))
                ps = str(round(playoffs_score[index], 2))
                ms = str(round(misc_score[index], 2))
                ks = str(round(kudos_score[index], 2))

                row_data = {"Player\nRank": rank, "Player\nName": name, "NBA-2K\nOVR": os,
                            "G-Score\n(G.O.A.T. Score)": gs, "R-Score\n(Regular Season)": rs, "P-Score\n(Playoffs)": ps, "K-Score\n(Awards)": ks, "M-Score\n(Misc.)": ms}

                data.append(row_data)
                i += 1

        df = pd.DataFrame(data)

        table_results = tabulate(
            df, headers="keys", tablefmt="html", showindex=False)

        inp_points_pergame /= 2
        inp_assists_pergame /= 2
        inp_rebounds_pergame /= 2
        inp_steals_pergame /= 2
        inp_blocks_pergame /= 2
        inp_three_pt_fieldgoal_pct /= 2
        inp_fieldgoal_pct /= 2
        inp_effective_fieldgoal_pct /= 2
        inp_true_shooting_pct /= 2
        inp_regular_szn_win_pct /= 2
        inp_playoffs_win_pct /= 2

        inp_championships /= 2
        inp_allstar_selections /= 2
        inp_regular_szn_mvps /= 2
        inp_finals_mvps /= 2
        inp_allstar_mvps /= 2
        inp_defensivePlayerOfTheYear /= 2
        inp_rookieOfTheYear /= 2
        inp_sixthManOfTheYear /= 2
        inp_mostImprovedPlayer /= 2
        inp_all_NBA_1stTeam /= 2
        inp_all_NBA_2ndTeam /= 2
        inp_all_NBA_3rdTeam /= 2
        inp_all_NBA_defensive_1stTeam /= 2
        inp_all_NBA_defensive_2ndTeam /= 2
        inp_all_NBA_rookie_1stTeam /= 2
        inp_all_NBA_rookie_2ndTeam /= 2

        inp_longevity /= 2
        inp_durability /= 2

        # Create a dictionary with variable names as keys and their values as values
        data_scorecard = {
            'PPG': [inp_points_pergame],
            'APG': [inp_assists_pergame],
            'RPG': [inp_rebounds_pergame],
            'SPG': [inp_steals_pergame],
            'BPG': [inp_blocks_pergame],
            '3FG': [inp_three_pt_fieldgoal_pct],
            'FG': [inp_fieldgoal_pct],
            'EFG': [inp_effective_fieldgoal_pct],
            'TS': [inp_true_shooting_pct],
            'RegularSeason_WL': [inp_regular_szn_win_pct],
            'Playoff_WL': [inp_playoffs_win_pct],
            'Playoff_Boost': [inp_playoffs_boost],
            'Championship_Boost': [inp_championship_boost_YN],
            'Champion_Boost Value': [4.0 if inp_championship_boost_YN == "Y" else 1.0],
            'Rings': [inp_championships],
            'All_Stars': [inp_allstar_selections],
            'RegularMVP': [inp_regular_szn_mvps],
            'FinalsMVP': [inp_finals_mvps],
            'AllStarMVP': [inp_allstar_mvps],
            'DPOY': [inp_defensivePlayerOfTheYear],
            'ROTY': [inp_rookieOfTheYear],
            '6MOY': [inp_sixthManOfTheYear],
            'MIP': [inp_mostImprovedPlayer],
            'NBA_1st_Team': [inp_all_NBA_1stTeam],
            'NBA_2nd_Team': [inp_all_NBA_2ndTeam],
            'NBA_3rd_Team': [inp_all_NBA_3rdTeam],
            '1st_Defense_Team': [inp_all_NBA_defensive_1stTeam],
            '2nd_Defense_Team': [inp_all_NBA_defensive_2ndTeam],
            '1st_Rookie_Team': [inp_all_NBA_rookie_1stTeam],
            '2nd_Rookie_Team': [inp_all_NBA_rookie_2ndTeam],
            'Longevity': [inp_longevity],
            'Durability': [inp_durability],
            'M-Score Penalty?': [inp_mScore_penalty_YN],
            'M-Score Penalty Value': [inp_mScore_penalty]
        }

        # Create a DataFrame from the dictionary
        df2 = pd.DataFrame(data_scorecard)

        transposed_df2 = df2.transpose()

        # Display the DataFrame as a table with borders
        table_scorecard = tabulate(
            transposed_df2, headers='keys', tablefmt='html')

        return render_template('table.html', table_results=table_results, table_scorecard=table_scorecard)

    return render_template('calculator.html')


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)
