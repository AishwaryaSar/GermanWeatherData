import requests
from bs4 import BeautifulSoup

# Send a request to the Wikipedia page listing German cities
url = 'https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population'
response = requests.get(url)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the list of cities
city_table = soup.find('table', {'class': 'wikitable'})
city_rows = city_table.find_all('tr')[1:]  # Skip the header row

# Extract city names
cities = [row.find_all('td')[1].text.strip() for row in city_rows]

# Save to file
with open('german_cities.txt','w') as file:
    file.write('\n'.join(cities))