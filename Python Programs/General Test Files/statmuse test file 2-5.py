import requests
from bs4 import BeautifulSoup
import re

str_start = 0
str_end = 0

pos1 = 0
pos2 = 0
pos3 = 0
pos4 = 0
pos5 = 0

#positions = ['point-guards']

stat = '3-point-percentage'

positions = ['point-guards', 'shooting-guards', 'small-forwards', 'power-forwards', 'centers']

years = ['1950', '1951', '1952', '1953', '1954', '1955', '1956', '1957', '1958', '1959', 
         '1960', '1961', '1962', '1963', '1964', '1965', '1966', '1967', '1968', '1969', 
         '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', 
         '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', 
         '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', 
         '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', 
         '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', 
         '2020', '2021', '2022', '2023']



for year in years:

    for position in positions:

        try:
            # URL to fetch HTML data from (using an f-string to insert position)
            url = f"https://www.statmuse.com/nba/ask/nba-league-average-{stat}-for-{position}-in-{year}"

            # HTML element tag to extract
            element_tag = "h1"  # Replace with the HTML element tag you want to extract

            # Send an HTTP GET request to the URL
            response = requests.get(url)

            if response.status_code == 422:
                avg = 0

            # Check if the request was successful (status code 200)
            elif response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, 'html.parser')

                # Find the specific element using the provided tag
                element = soup.find(element_tag)

                # Check if the element was found
                if element:
                    result = element.text.strip()  # Get the text within the element

                    num_result = re.findall(r'\d+\.\d+|\d+', result)

                    if position == 'point-guards':
                        pos1  = float(num_result[0])
                    elif position == 'shooting-guards':
                        pos2  = float(num_result[0])
                    elif position == 'small-forwards':
                        pos3  = float(num_result[0])
                    elif position == 'power-forwards':
                        pos4  = float(num_result[0])
                    elif position == 'centers':
                        pos5  = float(num_result[0])

                    avg = (pos1 + pos2 + pos3 + pos4 + pos5) / 5
                    avg = round(avg, 2)

                else:
                    print(f"{position}: Element not found on the page.")
            else:
                print(f"{position}: Failed to retrieve the page. Status code: {response.status_code}")
        except Exception as e:
            print(f"{position}: {str(e)}")

    print(f"{year},{avg},{stat}")
