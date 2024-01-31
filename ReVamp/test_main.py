from nba_api.stats.endpoints import playercareerstats
import mysql.connector
from datetime import datetime

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Bubblegum13',
    'database': 'nba_stats',
}

def fetch_and_insert_career_stats(player_id, player_name):
    # Fetch player career stats from NBA API
    career_stats = playercareerstats.PlayerCareerStats(player_id=player_id).get_data_frames()[0]

    # Connect to MySQL database
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    # Insert career stats into the database
    for _, row in career_stats.iterrows():
        # Insert data into the 'player_stats' table
        cursor.execute("""
            INSERT INTO player_stats (player_name, points, rebounds, assists)
            VALUES (%s, %s, %s, %s)
        """, (player_name, row['PTS'], row['REB'], row['AST']))

    # Commit changes and close the connection
    connection.commit()
    connection.close()

if __name__ == '__main__':
    # Replace 'your_player_id' with the actual NBA player ID
    player_id = 2544
    
    # Replace 'Player Name' with the actual player's name
    fetch_and_insert_career_stats(player_id=player_id, player_name='LeBron James')
