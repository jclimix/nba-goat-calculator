import requests
from bs4 import BeautifulSoup

# Define the player's ID (replace with the desired player's ID)
player_id = 2544  # Example player ID for LeBron James

# Define the URL for the player's advanced statistics
url = f"https://www.nba.com/stats/player/{player_id}/"

# Send an HTTP GET request to the URL
response = requests.get(url)

if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the specific element containing the advanced statistics
    # You need to inspect the webpage to locate the relevant HTML structure
    stats_element = soup.find('div', {'class': 'stats-player-summary'})

    if stats_element:
        # Extract and print the advanced statistics
        stats_text = stats_element.get_text()
        print(stats_text)
    else:
        print("Advanced statistics not found on the webpage.")
else:
    print(f"Failed to retrieve advanced statistics for Player ID {player_id}.")
