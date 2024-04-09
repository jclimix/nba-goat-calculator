import pygsheets
import pandas as pd

# Authorization
gc = pygsheets.authorize(service_file=r"C:\Users\jezei\OneDrive\Documents\Data Projects\NBA GOAT Project\ReVamp\keys\nba-goat-project-2577ff88fac0.json")

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['John', 'Steve', 'Sarah']

# Open the Google spreadsheet (where 'nba_goat_data1' is the name of my sheet)
sh = gc.open('nba_goat_data1')

# Select the first sheet
wks = sh[0]

# Update the first sheet with df, starting at cell B2.
wks.set_dataframe(df, start='B2')
