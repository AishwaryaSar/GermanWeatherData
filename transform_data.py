import json
import pandas as pd
from unidecode import unidecode

# access weather data from JSON file
with open('weather_data.json', 'r') as file:
    json_data = json.load(file)

appended_Data = []

# extract cityname, temprature, humidity, windspeed from the weather data
for data in json_data:
    city = unidecode(data['name'])
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    appended_Data.append([city, temperature, humidity, wind_speed])

# save the retrieved data in the form of a dataframe
weather_df = pd.DataFrame(appended_Data,columns=['City', 'Temperature', 'Humidity', 'Wind Speed'])

# save data as a CSV file 
weather_df.to_csv('weather_data.csv', index=False)