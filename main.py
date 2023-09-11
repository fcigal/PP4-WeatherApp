# importing libraries
from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from tkinter import ttk, messagebox
from datetime import datetime
import requests
import pytz


# Get weather condition button function.
def getWeather():
    try:
        # time and country information
        city = textbox1.get()
        geolocator = Nominatim(user_agent="my_WeatherApp")
        location = geolocator.geocode(city)
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
        print(result)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")  # 12 hours
        # current_time = local_time.strftime("%H:%M")  # 24 hours
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")
        # weather information
        your_api_key = ""  # Enter your Weather API Key
        api = f"https://api.openweathermap.org/data/2.5/weather?q={city},&appid={your_api_key}"

        json_data = requests.get(api).json()
        print(json_data)
        condition1 = json_data["weather"][0]["main"]
        description = json_data["weather"][0]["description"]
        temp = int(json_data["main"]["temp"] - 273.15)
        pressure = json_data["main"]["pressure"]
        humidity = json_data["main"]["humidity"]
        wind = json_data["wind"]["speed"]

        temperature.config(text=(temp, "°C"))
        condition.config(text=(condition1, "|", "FEELS", "LIKE", temp, "°C"))

        wind_text.config(text=wind)
        humidity_text.config(text=humidity)
        description_text.config(text=description)
        pressure_text.config(text=pressure)

    except Exception as e:
        messagebox.showerror("Weather App", "Please enter a valid city!!")


# Tk settings
weather_app = Tk()
weather_app.title("Weather App")
weather_app.geometry("1000x600")
weather_app.geometry("+300+250")
weather_app.resizable(False, False)

# GUI settings
# Search box image placing
search_img = PhotoImage(file="images/searchbox.png")
search_img_label = Label(image=search_img)
search_img_label.place(x=20, y=20)

# Search box text area placing
textbox1 = tk.Entry(weather_app, justify="center", width=20, font=("poppins", 25, "bold", "italic"), bg="white",
                    borderwidth=0, fg="#4c4b4b")
textbox1.place(x=50, y=50)
textbox1.focus()

# Search icon placing
search_icon_img = PhotoImage(file="images/searchicon.png")
search_icon = Button(image=search_icon_img, borderwidth=0, cursor="hand2", bg="white", border=0,
                     activebackground="white", command=getWeather)
weather_app.bind("<Return>", lambda event=None: getWeather())
search_icon.place(x=425, y=35)

# App logo placing
app_logo_img = PhotoImage(file="images/weatherlogo.png")
app_logo = Label(image=app_logo_img)
app_logo.place(x=300, y=140)

# Condition box placing
con_box_img = PhotoImage(file="images/bottom_box.png")
con_box = Label(image=con_box_img)
con_box.place(x=105, y=425)

# time
name = Label(weather_app, font=("arial", 22, "bold"))
name.place(x=40, y=140)
clock = Label(weather_app, font=("Helvetica", 20))
clock.place(x=40, y=180)

# Condition labels
label1 = Label(weather_app, text="WIND", font=("Helvatica", 18, "bold"), fg="white", bg="#29aae1")
label1.place(x=160, y=450)

label2 = Label(weather_app, text="HUMIDITY", font=("Helvatica", 18, "bold"), fg="white", bg="#29aae1")
label2.place(x=295, y=450)

label3 = Label(weather_app, text="DESCRIPTION", font=("Helvatica", 18, "bold"), fg="white", bg="#29aae1")
label3.place(x=475, y=450)

label4 = Label(weather_app, text="PRESSURE", font=("Helvatica", 18, "bold"), fg="white", bg="#29aae1")
label4.place(x=700, y=450)

temperature = Label(font=("arial", 70, "bold"), fg="#ee666d")
temperature.place(x=600, y=150)
condition = Label(font=("arial", 15, "bold"))
condition.place(x=600, y=250)

wind_text = Label(text="", font=("arial", 20, "bold"), bg="#29aae1")
wind_text.place(x=167, y=520)
humidity_text = Label(text="", font=("arial", 20, "bold"), bg="#29aae1")
humidity_text.place(x=337, y=520)
description_text = Label(text="", font=("arial", 20, "bold"), bg="#29aae1")
description_text.place(x=450, y=520)
pressure_text = Label(text="", font=("arial", 20, "bold"), bg="#29aae1")
pressure_text.place(x=740, y=520)

weather_app.mainloop()
