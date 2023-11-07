#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

years = list(range(1960,2024))

url_start = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

for year in years:
        url = url_start.format(year)
        data = requests.get(url)

        with open ("per_game_data/{}.html".format(year), "w+") as f:
                f.write(data.text)

with open("per_game_data/1960.html") as f:
        page = f.read()

#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
page_to_scrape = requests.get("https://www.basketball-reference.com/leagues/NBA_1960_per_game.html")

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE
soup = BeautifulSoup(page, 'html.parser')

#FIND ALL THE ITEMS IN THE PAGE WITH A CLASS ATTRIBUTE OF 'TEXT'
#AND STORE THE LIST AS A VARIABLE
per_game_table = soup.find(id="div_per_game_stats")

import pandas as pd

per_game_table1960 = pd.read_html(str(per_game_table))[0]

per_game_table1960