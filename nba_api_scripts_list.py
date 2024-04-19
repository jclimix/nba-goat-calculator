from nba_api.stats.endpoints import playercareerstats
import pandas as pd

def calculate_efg(stats_df):
    eFG = (stats_df['FGM'] + 0.5 * stats_df['FG3M']) / stats_df['FGA']
    stats_df['eFG'] = round(eFG, 3)
    return stats_df

def calculate_ts(stats_df):
    FGA = stats_df['FGA']
    FTA = stats_df['FTA']
    PTS = stats_df['PTS']
    
    TS = PTS / (2 * (FGA + 0.44 * FTA))
    stats_df['TS'] = round(TS, 3)
    return stats_df

def get_career_stats(player_id):
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id, per_mode36='PerGame')
    
    regular_szn_stats = career_stats.get_data_frames()[1]
    postseason_stats = career_stats.get_data_frames()[3]
    career_log = career_stats.get_data_frames()[0]

    years = len(career_log)
    
    regular_szn_stats = calculate_efg(regular_szn_stats)
    postseason_stats = calculate_efg(postseason_stats)
    
    regular_szn_stats = calculate_ts(regular_szn_stats)
    postseason_stats = calculate_ts(postseason_stats)
    
    return regular_szn_stats, postseason_stats, years

def main():
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_colwidth', None)

    # Example player ID (LeBron James)
    player_id = '2544'
    
    regular_szn_stats, postseason_stats, years = get_career_stats(player_id)
    print("Regular Season Stats:")
    print(regular_szn_stats)
    print("\nPostseason Stats:")
    print(postseason_stats)
    print("\nYears:")
    print(years)

if __name__ == "__main__":
    main()
