import requests
from bs4 import BeautifulSoup

def scrape_nba_stats(url):
    # Send a GET request to the URL
    response = requests.get(url)

    # Check if request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all elements with class "Crom_base__f0niE"
        elements = soup.find_all(class_="Crom_base__f0niE")
        
        # Return the found elements
        return elements
    else:
        print("Failed to retrieve webpage.")
        return None

# URL of the NBA stats page
url = "https://www.nba.com/stats/player/2544/advanced?SeasonType=Regular+Season"

# Scrape the webpage and print the found elements
scraped_elements = scrape_nba_stats(url)
if scraped_elements:
    for element in scraped_elements:
        print(element)
