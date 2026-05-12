# This program asks user for a city and shows weather in terminal

from weatherAPI import get_weather
# imports weather function from API file

city = input("Enter city: ")
# asks user to type a city name

data = get_weather(city)
# gets weather data from API

if data["cod"] == 200:
# checks if API request was successful (200 = OK)

    print(f"\nWeather in {data['name']}")
    # shows city name

    print(f"Temperature: {data['main']['temp']}°C")
    # shows temperature

    print(f"Condition: {data['weather'][0]['description']}")
    # shows weather condition

    print(f"Humidity: {data['main']['humidity']}%")
    # shows humidity

else:
# runs if API fails

    print("Failed to get weather data")
    # error message