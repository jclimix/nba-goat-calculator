import sqlite3
from google.cloud import storage
import pandas as pd
import numpy as np
from datetime import datetime
import mysql.connector
import sys
from pandasql import sqldf


cnx = mysql.connector.connect(user='root', password='sqlpass11$', host='34.28.148.219', database='nba_db')

cursor = cnx.cursor()
query1 = ("select * from test_player_stats")
cursor.execute(query1)
df = pd.DataFrame(cursor.fetchall())

columns = ['PLAYER_ID', 'PLAYER_NAME', 'R_PPG', 'R_APG', 'R_RPG', 'R_SPG', 'R_BPG', 'R_FG', 'R_eFG', 'R_TS',
           'P_PPG', 'P_APG', 'P_RPG', 'P_SPG', 'P_BPG', 'P_FG', 'P_eFG', 'P_TS']

df.columns = columns

print(df)

total_col = sum(df['R_PPG'])

print(total_col)