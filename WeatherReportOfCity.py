from tkinter import *
import requests 
import json 

root = Tk() 
root.title("Weather Report") 
root.geometry("500x500") 
root['background'] = "red"

getAndShowWeather = StringVar() 
cityName = Entry(root, textvariable = getAndShowWeather, font = ("bold", 15), width = 20) 
cityName.place(x = 165, y = 1)  
    
def getAndShowWeather(): 
    api_request = requests.get("https://api.openweathermap.org/data/2.5/weather?q="+ cityName.get() + "&units=metric&appid=23c6825e66f08d003c4c88c4a23ba46a") 
    data = json.loads(api_request.content) 

    main = data['main'] 
    currentTemprature = main['temp'] 
    currentHumidity = main['humidity'] 

    lableTemperature.configure(text = str(currentTemprature) + chr(176) + "C.") 
    lableHumidity.configure(text = str(currentHumidity) + "%.") 
  
Label(root, text = "Enter city name: ", font = ("bold", 15)).place(x = 0, y = 0)

cityNameButton = Button(root, text = "search", font = ("bold", 15), command = getAndShowWeather) 
cityNameButton.place(x = 200, y = 40) 

temperatureHeading = Label(root, text = "Temperature: ", width = 0, bg = "white", font = ("bold", 15)) 
temperatureHeading.place(x = 20, y = 90) 
  
lableTemperature = Label(root, text = "...", width = 0, bg = "white", font = ("bold", 15)) 
lableTemperature.place(x = 150, y = 90) 
  
humidityHeading = Label(root, text = "Humidity: ", width = 0, bg = "white", font = ("bold", 15)) 
humidityHeading.place(x = 20, y = 120) 
  
lableHumidity = Label(root, text = "...", width = 0, bg = "white", font = ("bold", 15)) 
lableHumidity.place(x = 107, y = 120)  

root.mainloop() 
