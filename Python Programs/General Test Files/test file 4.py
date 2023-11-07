#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

years = list(range(2020,2024))

url_start = "https://www.basketball-reference.com/leagues/NBA_{}_advanced.html"

for year in years:
        url = url_start.format(year)
        data = requests.get(url)

        with open ("advgamedata/{}.html".format(year), "w+", encoding="utf-8") as f:
                f.write(data.text)

with open("advgamedata/1950.html", encoding="utf-8") as f:
        page = f.read()

soup = BeautifulSoup(page, 'html.parser')

per_game_table = soup.find(id="div_advanced_stats")

import pandas as pd

game_table = pd.read_html(str(per_game_table))

print(game_table)