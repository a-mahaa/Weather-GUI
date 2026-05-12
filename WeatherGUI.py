# This program creates a weather app with a graphical window (GUI)

import tkinter as tk
# creates windows, buttons, labels

from tkinter import messagebox
# allows popup messages

from weatherAPI import get_weather
# imports API function

def search_weather():
# runs when button is clicked

    city = city_entry.get()
    # gets text from input box

    if city == "":
    # checks if user did not type anything

        messagebox.showwarning("Error", "Please enter a city")
        # shows warning popup

        return
        # stops function

    data = get_weather(city)
    # gets weather data from API

    if data["cod"] == 200:
    # checks if API worked

        city_result.config(text=f"Weather in {data['name']}")
        # shows city name

        temp_result.config(text=f"Temperature: {data['main']['temp']}°C")
        # shows temperature

        condition_result.config(text=f"Condition: {data['weather'][0]['description']}")
        # shows weather condition

        humidity_result.config(text=f"Humidity: {data['main']['humidity']}%")
        # shows humidity

    else:
    # if API fails

        messagebox.showerror("Error", "Could not get weather data")
        # error popup

root = tk.Tk()
# creates main window

root.title("Weather App")
# sets window title

root.geometry("400x300")
# sets window size

title = tk.Label(root, text="Weather App", font=("Arial", 16))
# title text

title.pack(pady=10)
# displays title

city_entry = tk.Entry(root, font=("Arial", 14))
# input box for city

city_entry.pack(pady=10)
# places input box

btn = tk.Button(root, text="Get Weather", command=search_weather)
# button that runs function

btn.pack(pady=10)
# places button

city_result = tk.Label(root, text="")
# label for city

city_result.pack()

temp_result = tk.Label(root, text="")
# label for temperature

temp_result.pack()

condition_result = tk.Label(root, text="")
# label for condition

condition_result.pack()

humidity_result = tk.Label(root, text="")
# label for humidity

humidity_result.pack()

root.mainloop()
# keeps window open
