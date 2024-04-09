#Accessing Weather API

import datetime
import requests

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = "dfb8aeb3e4fe220f8b8d85a9843901b5"

CITY = "Los Angeles"


def kelvin_to_celcsius_fahrenite(kelvin):   
    celcius = kelvin - 273.15
    fahrenite = celcius * (9/5) + 32
    return celcius,fahrenite


url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()

temp_kelvin = response['main']['temp']
temp_celcsius, temp_fahrenite = kelvin_to_celcsius_fahrenite(temp_kelvin)

feels_like_kelvin = response['main']['feels_like']
feels_like_celcius, feels_like_fahrenite = kelvin_to_celcsius_fahrenite(feels_like_kelvin)

windspeed = response['wind']['speed']

humidity = response['main']['humidity']
description = response['weather'][0]['description']

sunrise_time = datetime.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
sunset_time = datetime.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

print(f"Temprature in {CITY}: {temp_celcsius:.2f}°C or {temp_fahrenite:.2f}°F")
print(f"Temprature in {CITY} feels like: {feels_like_celcius:.2f}°C or {feels_like_fahrenite:.2f}°F")
print(f"Humidity in {CITY}: {humidity}%")
print(f"Wind Speed in {CITY}: {windspeed}m/s")
print(f"Sun rises in {CITY} at {sunrise_time} local time")
print(f"Sun sets in {CITY} at {sunset_time} local time")
print(f"General Weather in {CITY}: {description}")

