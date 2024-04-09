from nba_api.stats.endpoints import commonallplayers, playerindex
import sqlite3
from datetime import datetime

db_file = 'C:\\Users\\jezei\\Downloads\\sqlite-tools-win-x64-3450100\\nba.db'

def get_all_players_ids():
    all_players_info = commonallplayers.CommonAllPlayers().get_data_frames()[0]
    return all_players_info['PERSON_ID'].tolist()

def get_player_info(player_id):
    player_index = playerindex.PlayerIndex(player_id).get_data_frames()[0]
    if not player_index.empty:
        return player_index.iloc[0]
    return None

def insert_all_players_info():
    try:
        all_player_ids = get_all_players_ids()

        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        for player_id in all_player_ids:
            player_info = get_player_info(player_id)

            if player_info is not None:
                player_name = player_info['DISPLAY_FIRST_LAST']
                active_status = player_info['ACTIVE_STATUS']

                existing_record = cursor.execute("SELECT id FROM player_info WHERE id = ?", (player_id,)).fetchone()

                if existing_record:
                    print(f"Player with ID {player_id} already exists in the database. You might want to update the record.")
                else:
                    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Inserting data into 'player_info' table for {player_name} at {current_date}")

                    cursor.execute("""
                        INSERT INTO player_info (id, player_name, is_active, update_date)
                        VALUES (?, ?, ?, ?)
                    """, (player_id, player_name, active_status, current_date))

        connection.commit()
        connection.close()

        print("Data successfully inserted into the database for all NBA players.")

    except Exception as e:
        print(f"An error occurred: {e}")

def view_player_info():
    try:
        connection = sqlite3.connect(db_file)
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM player_info")
        player_info_data = cursor.fetchall()

        if player_info_data:
            print("Player Information:")
            for row in player_info_data:
                print(f"ID: {row[0]}, Player Name: {row[1]}, Is Active: {row[2]}, Update Date: {row[3]}")
        else:
            print("No player information found in the 'player_info' table.")

        connection.close()

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == '__main__':
    insert_all_players_info()

    view_player_info()
