#! /usr/bin/python3
# quickWeather.py - Prints the weather for a location from the command line..

import json, sys, requests

# Compute location from command line arguments
if len(sys.argv) < 2:
    print("Usage: quickWeather.py location")
    sys.exit()

location = ' '.join(sys.argv[1:])

# Download the Json data from OpenWeatherMap.org API
url = 'http://api.openweathermap.org/data/2.5/weather?q=%s&appid=2756c9404e1983a8fa8f76ebccf04a6c' % location
response = requests.get(url)
response.raise_for_status()

weatherData = json.loads(response.text)
data = weatherData['weather']
print('Current weather in %s:' % (location))
print(data[0]['main'], "-", data[0]['description'])

temp = weatherData['main']
print("Temperature is:", temp['temp']-273.15, "°C")
print()
