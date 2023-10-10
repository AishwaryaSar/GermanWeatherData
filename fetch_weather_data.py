# Extract data from a public API OpenWeatherMap API https://openweathermap.org/api
import requests
import json

# key to access openweathermap api
# login to openweathermap and request for an api key
API_KEY = 'replace-with-your-api-key'
weather_data = []

#retrieve list of cities to fetch weather data
with open('german_cities.txt','r') as file:
    cities = file.read().splitlines()

# clean city names for api usage and fetch data
for city in cities:
    #preprocess to remove subtext with german words
    if "(" in city:
        index = city.index("(")
        city_name = city[:index-1].strip()
    else : city_name = city
    URL = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}'
    response = requests.get(URL)
    result = response.json()
    weather_data.append(result)

# save the extracted weather data to a JSON file
with open('weather_data.json','w') as outputFile:
     json.dump(weather_data,outputFile)