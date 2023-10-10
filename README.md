# GermanWeatherData
This project focuses on gathering weather data for cities in Germany using various data engineering techniques. The process involves web scraping, API integration, data transformation, and loading the data into a SQLite database.

## Files

- **`fetch_city.py`**: This script scrapes a Wikipedia page to retrieve a list of German cities by population and saves them to a text file.

- **`fetch_weather_data.py`**: This script uses the OpenWeatherMap API to fetch weather data for the cities listed in `german_cities.txt` and stores the results in a JSON file.

- **`transform_data.py`**: This script processes the JSON data containing weather information, extracts relevant fields, and creates a structured DataFrame. The data is then saved as a CSV file.

- **`load_data.py`**: This script establishes a connection to an SQLite database, creates a table, and populates it with the weather data stored in `weather_data.csv`.

## Usage

1. **Extracting Cities:**

   ```bash
   python fetch_city.py

- This script scrapes Wikipedia to obtain a list of German cities by population and saves it in `german_cities.txt`.

2. **Fetching Weather Data:**

   ```bash
   python fetch_weather_data.py

- This script uses the OpenWeatherMap API to gather weather data for the cities listed in `german_cities.txt` and stores the results in `weather_data.json`.

3. **Transforming Data:**

   ```bash
   python transform_data.py

- This script processes the JSON data, extracts city names, temperature, humidity, and wind speed, and creates a structured CSV file named `weather_data.csv`.

4. **Loading Data:**

   ```bash
   python load_data.py

- This script establishes a connection to an SQLite database, creates a table `germany_weather_data`, and populates it with the data from `weather_data.csv`.

## Prerequisites
- Python 3.x
- Libraries: `requests`, `beautifulsoup4`, `pandas`, `unidecode`, `sqlite3`
- API key from [OpenWeatherMap](https://openweathermap.org/api)

## Acknowledgments

- [OpenWeatherMap API](https://openweathermap.org/api) for providing the weather data.
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) for web scraping capabilities.
- [pandas](https://pandas.pydata.org/) for data manipulation and analysis.
- [unidecode](https://pypi.org/project/Unidecode/) for text normalization.
- [Wikipedia](https://www.wikipedia.org/) for providing the list of German cities.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

