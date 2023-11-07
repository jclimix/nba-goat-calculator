import requests
from bs4 import BeautifulSoup

# Step 1: Define the URL of the webpage you want to scrape
url = "https://www.statmuse.com/nba/ask/nba-league-average-ppg-per-position-in-1973"

# Step 2: Send an HTTP GET request to the webpage and get the HTML content
response = requests.get(url)

# Step 3: Check if the request was successful (status code 200)
if response.status_code == 200:
    # Step 4: Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Step 5: Use BeautifulSoup to find and extract the data you need
    # Here, we are looking for all <h2> elements with a specific class attribute
    headline_elements = soup.find_all('td', class_='text-right px-2 py-1 bg-white')

    # Step 6: Extract and print the headlines
    for headline in headline_elements:
        # Use .text to extract the text content of the <h2> element
        print(headline.text)
else:
    print("Failed to retrieve data. Status code:", response.status_code)
