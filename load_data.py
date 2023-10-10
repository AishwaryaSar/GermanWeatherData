import sqlite3
import csv

# Connect to the SQLite database
conn = sqlite3.connect('weather_data.db')
cursor = conn.cursor()

# Create a table if it doesn't exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS germany_weather_data (
        city TEXT,
        temperature REAL,
        humidity INTEGER,
        windspeed REAL
    )
''')

# Extract values from the CSV file and insert them into the table
with open('weather_data.csv','r')as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        cursor.execute('''
            INSERT INTO germany_weather_data (city, temperature, humidity, windspeed)
            VALUES (?, ?, ?, ?)
        ''', (row['City'], row['Temperature'], row['Humidity'], row['Wind Speed']))

# Commit changes and close connection
conn.commit()
conn.close()
