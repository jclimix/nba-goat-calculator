from flask import Flask, render_template, request
from pprint import pprint
import pandas as pd
from tabulate import tabulate
from waitress import serve

app = Flask(__name__)


class Player:
    def __init__(self, data) -> None:
        self.data = data


class Calculator:
    def __init__(self) -> None:
        pass

    def read_csv_as_dataframe(self, csv_file_path) -> pd.DataFrame:
        try:
            df = pd.read_csv(csv_file_path)
            return df
        except FileNotFoundError:
            print(f"Error: File '{csv_file_path}' not found.")
            return None
        except Exception as e:
            print(f"An error occurred while reading the CSV file 'csv_file_path': {e}")
            return None

    def create_players_from_dataframe(self, dataframe):
        players = []
        for _, row in dataframe.iterrows():
            player_data = row.to_dict()
            player = Player(player_data)
            players.append(player)
        return players


calc = Calculator()


@app.route('/', methods=['GET', 'POST'])
def find_goat_web():
    if request.method == 'POST':

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
        idx = dataframe['INDEX']
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
        all_nba_1st_team = dataframe['NBAT1']
        all_nba_2nd_team = dataframe['NBAT2']
        all_nba_3rd_team = dataframe['NBAT3']
        allstar_mvps = dataframe['ALLSTARMVPS']
        defensive_player_of_year = dataframe['DPOYS']
        rookie_of_years = dataframe['ROTYS']
        sixth_man_of_years = dataframe['SMOYS']
        mostImprovedPlayer = dataframe['MIPS']
        all_nba_defensive_1st_team = dataframe['DEFT1']
        all_nba_defensive_2nd_team = dataframe['DEFT2']
        all_nba_rookie_1st_team = dataframe['ROOKT1']
        all_nba_rookie_2nd_team = dataframe['ROOKT2']
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
        inp_defensive_player_of_year = float(request.form['inp_dpoy'])
        inp_rookie_of_year = float(request.form['inp_roty'])
        inp_sixth_man_of_year = float(request.form['inp_smoy'])
        inp_most_improved_player = float(request.form['inp_mip'])
        inp_all_nba_1st_team = float(request.form['inp_1T'])
        inp_all_nba_2nd_team = float(request.form['inp_2T'])
        inp_all_nba_3rd_team = float(request.form['inp_3T'])
        inp_all_nba_defensive_1st_team = float(request.form['inp_1DT'])
        inp_all_nba_defensive_2nd_team = float(request.form['inp_2DT'])
        inp_all_nba_rookie_1st_team = float(request.form['inp_1RT'])
        inp_all_nba_rookie_2nd_team = float(request.form['inp_2RT'])

        inp_kudos_score_boost = float(request.form['inp_k_bst'])

        inp_longevity = float(request.form['inp_long'])
        inp_durability = float(request.form['inp_dur'])
        inp_m_score_penalty_yn = (request.form['inp_ms_penalty'])
        inp_m_score_penalty = float(request.form['inp_pen'])

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
        inp_defensive_player_of_year = float(inp_defensive_player_of_year)
        inp_rookie_of_year = float(inp_rookie_of_year)
        inp_sixth_man_of_year = float(inp_sixth_man_of_year)
        inp_most_improved_player = float(inp_most_improved_player)
        inp_all_nba_1st_team = float(inp_all_nba_1st_team)
        inp_all_nba_2nd_team = float(inp_all_nba_2nd_team)
        inp_all_nba_3rd_team = float(inp_all_nba_3rd_team)
        inp_all_nba_defensive_1st_team = float(inp_all_nba_defensive_1st_team)
        inp_all_nba_defensive_2nd_team = float(inp_all_nba_defensive_2nd_team)
        inp_all_nba_rookie_1st_team = float(inp_all_nba_rookie_1st_team)
        inp_all_nba_rookie_2nd_team = float(inp_all_nba_rookie_2nd_team)

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
        inp_defensive_player_of_year *= 2
        inp_rookie_of_year *= 2
        inp_sixth_man_of_year *= 2
        inp_most_improved_player *= 2
        inp_all_nba_1st_team *= 2
        inp_all_nba_2nd_team *= 2
        inp_all_nba_3rd_team *= 2
        inp_all_nba_defensive_1st_team *= 2
        inp_all_nba_defensive_2nd_team *= 2
        inp_all_nba_rookie_1st_team *= 2
        inp_all_nba_rookie_2nd_team *= 2

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
                               (all_nba_1st_team[i] * inp_all_nba_1st_team * 1.5) +
                               (all_nba_2nd_team[i] * inp_all_nba_2nd_team * 1.5) +
                               (all_nba_3rd_team[i] * inp_all_nba_3rd_team * 1.5) +
                               (defensive_player_of_year[i] * inp_defensive_player_of_year * inp_defensive_boost * 1.5) +
                               (rookie_of_years[i] * inp_rookie_of_year * 1.5) +
                               (sixth_man_of_years[i] * inp_sixth_man_of_year * 1.5) +
                               (allstar_mvps[i] * inp_allstar_mvps * 1.5) +
                               (all_nba_defensive_1st_team[i] * inp_all_nba_defensive_1st_team * inp_defensive_boost * 1.5) +
                               (all_nba_defensive_2nd_team[i] * inp_all_nba_defensive_2nd_team * inp_defensive_boost * 1.5) +
                               (all_nba_rookie_1st_team[i] * inp_all_nba_rookie_1st_team * 1.5) +
                               (all_nba_rookie_2nd_team[i] * inp_all_nba_rookie_2nd_team * 1.5)) * .8) * inp_kudos_score_boost

            # M-Score
            misc_score[i] = ((((years[i] * 2) * inp_longevity) +
                             ((games[i] / 10) * inp_durability)) / 2) * 1.1

            # GOAT-Score

            # Select GOAT-Score Function
            if inp_m_score_penalty_yn == "Y":

                goat_score[i] = (reg_szn_score[i] + playoffs_score[i] + kudos_score[i] +
                                 era_score[i]) - (misc_score[i] * float(inp_m_score_penalty))

            if inp_m_score_penalty_yn == "N":

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
        inp_defensive_player_of_year /= 2
        inp_rookie_of_year /= 2
        inp_sixth_man_of_year /= 2
        inp_most_improved_player /= 2
        inp_all_nba_1st_team /= 2
        inp_all_nba_2nd_team /= 2
        inp_all_nba_3rd_team /= 2
        inp_all_nba_defensive_1st_team /= 2
        inp_all_nba_defensive_2nd_team /= 2
        inp_all_nba_rookie_1st_team /= 2
        inp_all_nba_rookie_2nd_team /= 2

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
            'DPOY': [inp_defensive_player_of_year],
            'ROTY': [inp_rookie_of_year],
            '6MOY': [inp_sixth_man_of_year],
            'MIP': [inp_most_improved_player],
            'NBA_1st_Team': [inp_all_nba_1st_team],
            'NBA_2nd_Team': [inp_all_nba_2nd_team],
            'NBA_3rd_Team': [inp_all_nba_3rd_team],
            '1st_Defense_Team': [inp_all_nba_defensive_1st_team],
            '2nd_Defense_Team': [inp_all_nba_defensive_2nd_team],
            '1st_Rookie_Team': [inp_all_nba_rookie_1st_team],
            '2nd_Rookie_Team': [inp_all_nba_rookie_2nd_team],
            'Longevity': [inp_longevity],
            'Durability': [inp_durability],
            'M-Score Penalty?': [inp_m_score_penalty_yn],
            'M-Score Penalty Value': [inp_m_score_penalty]
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
    serve(app, host="0.0.0.0", port=8001)
