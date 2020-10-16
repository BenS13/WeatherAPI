from datetime import datetime
import requests, json
import sanatiseOutput


def getWeather(city):
    url = "http://api.openweathermap.org/data/2.5/weather?"
    paremeters = {'q':city, 'appid' : 'a140b36a4e11dbbbdbb81cba515ef85e', 'units': 'metric'}
    r = requests.get(url, params=paremeters)
    loc = "City: ", r.json()['name']
    temp = "Temperature: ", r.json()['main']['temp']
    feelsLike = "Feels Like: ",r.json()['main']['feels_like']
    time = "Current Time: ", datetime.fromtimestamp(r.json()['dt'])
    tempMin = "Minimum Temp: ", r.json()['main']['temp_min']
    tempMax = "Maximum Temp: ", r.json()['main']['temp_max']
    sanatiseOutput.sanatiseOutput(loc)         #r.json[tree][sub-tree] to locate data
    sanatiseOutput.sanatiseOutput(temp)
    sanatiseOutput.sanatiseOutput(tempMin)
    sanatiseOutput.sanatiseOutput(tempMax)
    sanatiseOutput.sanatiseOutput(feelsLike)
    sanatiseOutput.sanatiseOutput(time)


