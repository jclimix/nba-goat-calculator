#get player info

#fill player info

#this is the test code to pull data from the NBA site using the nba_api and storing it into a SQL database
from nba_api.stats.static import players
import mysql.connector
from datetime import datetime

# MySQL database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Bubblegum13',
    'database': 'nba_stats',
}

def fetch_and_insert_career_stats(player_id):
    try:

        #Get all players
        players_list = #endpoint to get all players in df

        # Get player name
        player_info = players.find_player_by_id(player_id)
        player_name = player_info['full_name']

        active_status = 1

        # Connect to MySQL database
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Insert current date and time
        current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"Inserting data into 'player_info' table for {player_name} at {current_date}")

        # Insert career stats into the database
        for _, row in players_list.iterrows():
            cursor.execute("""
                INSERT INTO player_info (id, player_name, is_active, update_date)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (player_id, player_name, active_status, current_date))

        # Commit changes and close the connection
        connection.commit()
        connection.close()

        print("Data successfully inserted into the database.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    # Replace 'your_player_id' with the actual NBA player ID
    player_id = 2544
    
    fetch_and_insert_career_stats(player_id=player_id)

