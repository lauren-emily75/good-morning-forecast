#! python3
# quickWeather.py - Prints the weather for a location from the cmd line
import requests, json, sys, time
from win10toast import ToastNotifier
import pyttsx3

image_dir = './Imgs/'

weather_imgs = {
    '01': 'clear.ico',
    '02': 'few_cloud.ico',
    '03': 'scatter_cloud.ico',
    '04': 'broken_cloud.ico',
    '09':'shower_rain.ico',
    '10': 'rain.ico',
    '11': 'thunder.ico',
    '13': 'snow.ico',
    '50': 'mist.ico'
}

# compute location from cmd line args
if len(sys.argv) < 2:
    print('Usage: good_morning.py location')
    sys.exit()

location = ' '.join(sys.argv[1:])
API_KEY = open('key.txt', 'r').read()

query_params = {
    'q': location,
    'APPID': API_KEY
}

# download json data from OpenWeatherMap.orgs API
url = 'http://api.openweathermap.org/data/2.5/forecast'
response = requests.get(url, params=query_params)
# check download ok
response.raise_for_status()
# load JSON into python var
weatherData = json.loads(response.text)

img_code = weatherData['list'][0]['weather'][0]['icon'][:-1]


def kelvinToCel(tempKel):
    return round(tempKel - 273.15, 2)


w = weatherData['list']
main_weather = w[0]['weather'][0]['main']
desc = w[0]['weather'][0]['description']
temp = kelvinToCel(w[0]["main"]["temp"])

weather_str = f"""The weather forecast in {location} today is:
{main_weather.title()} - {desc.title()}
Temp - {temp} degrees"""

# show notification
toaster = ToastNotifier()
toaster.show_toast('Good Morning <Your Name>!', weather_str, threaded= True, icon_path=image_dir + weather_imgs.get(img_code), duration=10)

morning_greeting = f'Good morning <Your name>! The weather forecast in {location} today is {desc.title()},' \
                   f'with a temperature of {temp} degrees'
# Initialize the converter
converter = pyttsx3.init()
converter.setProperty('rate', 190)
converter.setProperty('volume', 0.7)
converter.say(morning_greeting)
converter.runAndWait()
