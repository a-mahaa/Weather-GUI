# This program connects to the OpenWeather API and gets weather data for a city

import requests  # lets Python talk to websites (APIs)

API_KEY = "472ad775865e82e6b711fca01ae4a756"
# your teacher's API key (used to access weather service)

def get_weather(city):
# function that takes a city name and returns weather data

    url = "https://api.openweathermap.org/data/2.5/weather"
    # base API link for current weather

    params = {
        "q": city,
        # city name user types

        "appid": API_KEY,
        # authentication key for API

        "units": "metric"
        # gives temperature in Celsius
    }

    response = requests.get(url, params=params)
    # sends request to weather website

    return response.json()
    # converts response into Python dictionary and returns it