from nba_api.stats.static import players
from nba_api.stats.endpoints import playercareerstats
import pandas as pd

# Define the player ID you're interested in
player_id = 76173;  # Change this to the desired player's ID

# Get playoff career stats for the player
playoff_career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
playoff_career_stats_df = playoff_career_stats.get_data_frames()[2]

# Get career stats
career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
career_stats_df = career_stats.get_data_frames()[2]  # Index 1 corresponds to postseason stats

if len(career_stats_df) == 0:
    print("No postseason stats found for the player.")
else:
    # Write postseason stats to a file
    output_file = "charlie_black_stats.csv"
    career_stats_df.to_csv(output_file, index=False)
    print("postseason stats written to", output_file)