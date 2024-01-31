import mysql.connector
from nba_api.stats.static import players
import pandas as pd
from datetime import datetime

def get_all_nba_players():
    # Get all NBA players using the nba_api
    nba_players = players.get_players()

    # Create a DataFrame from the list of players
    df = pd.DataFrame(nba_players)

    return df

# Call the function to get the DataFrame with all NBA players
all_players_df = get_all_nba_players()

# Display the DataFrame
print(all_players_df)

# Add an 'update_date' column with the current date and time
all_players_df['update_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# MySQL database connection
cnx = mysql.connector.connect(user='root', password='sqlpass11$', host='34.28.148.219', database='nba_db')
cursor = cnx.cursor()

# Loop through the DataFrame and insert each row into the MySQL database
table_name = 'player_info'
for index, row in all_players_df.iterrows():
    # Assuming 'player_info' is the table name in the database
    query = f"INSERT INTO {table_name} (column1, column2, column3, column4, column5, update_date) VALUES (%s, %s, %s, %s, %s, %s)"
    
    # Handle NaN values by replacing them with None
    values = tuple([None if pd.isna(value) else value for value in row])
    
    # Append the current date and time to the values tuple
    values += (all_players_df.loc[index, 'update_date'],)
    
    cursor.execute(query, values)

# Commit changes and close the database connection
cnx.commit()
cnx.close()
