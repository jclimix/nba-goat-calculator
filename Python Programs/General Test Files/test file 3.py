#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

years = list(range(1950,1960))

url_start = "https://www.basketball-reference.com/leagues/NBA_{}_per_game.html"

for year in years:
        url = url_start.format(year)
        data = requests.get(url)

        with open ("pergamedata/{}.html".format(year), "w+", encoding="utf-8") as f:
                f.write(data.text)

with open("pergamedata/1960.html", encoding="utf-8") as f:
        page = f.read()

soup = BeautifulSoup(page, 'html.parser')

per_game_table = soup.find(id="div_per_game_stats")

import pandas as pd

game_table = pd.read_html(str(per_game_table))

print(game_table)