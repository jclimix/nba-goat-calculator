import pandas as pd

player_count = 4815

def read_csv_as_dataframe(csv_file_path):
    """
    Reads a CSV file and returns it as a pandas DataFrame.
    
    Args:
    csv_file_path (str): The file path to the CSV file.
    
    Returns:
    pandas.DataFrame: DataFrame containing the data from the CSV file.
    """
    try:
        df = pd.read_csv(csv_file_path)
        return df
    except FileNotFoundError:
        print(f"Error: File '{csv_file_path}' not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Example usage:
if __name__ == "__main__":
    
    csv_file_path = "jmg-nba-dataset-prod.csv"  # Change this to your CSV file path
    dataframe = read_csv_as_dataframe(csv_file_path)
    if dataframe is not None:

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


        #aggregated arrays
        r_score = [0] * player_count
        p_score = [0] * player_count
        k_score = [0] * player_count
        m_score = [0] * player_count
        era_score = [0] * player_count
        goat_score = [0] * player_count

        print(player_name[2075])