#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import json
import requests
import sys

# Compute location from clis.
if len(sys.argv) < 3:
    print('Usage: getOpenWeather.py API key, city_name, 2-letter_country_code')
    sys.exit()

APPID = sys.argv[1]
location = ' '.join(sys.argv[2:])

# Download the json data from OpenWeatherMap.org API
url = 'https://api.openweathermap.org/data/2.5/forecast?q={}&appid={}&units=metric'.format(location, APPID)
response = requests.get(url)
response.raise_for_status()
#print(response.text)
# Load JSON data into a python variable
weatherData = json.loads(response.text)

# Print weather descriptions
w = weatherData['list']
print('Current weather in {}'.format(location))
print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'], 'at', w[0]['main']['temp'] ,'degrees.')
for i in range(1, len(weatherData)):
    print(f'Forecast for today + {i} days:')
    print(w[i]['weather'][0]['main'], '-', w[i]['weather'][0]['description'], 'at', w[i]['main']['temp'] ,'degrees.')



