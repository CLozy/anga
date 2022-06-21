
import requests
import re
from bs4 import BeautifulSoup

from datetime import datetime as dt

# def weather_data(city):

#     USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
#     LANGUAGE = "en-KE,en;q=0.5"

#     URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
#     URL+= city

#     session = requests.Session()
#     session.headers['User-Agent'] = USER_AGENT
#     session.headers['Accept-Language'] = LANGUAGE
#     session.headers['Content-Language'] = LANGUAGE
#     html = session.get(URL)
#     # create a new soup
#     soup = BeautifulSoup(html.text, "html.parser")

#         # store all results on this dictionary
#     result = {}
#     # extract region
#     result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text

#     #get temp in celsius and farenheit

#     result['temp_now_c'] = soup.find("span", attrs={"id": "wob_tm"}).text + "°C"
#     result['temp_now_f'] = soup.find("span", attrs={"id": "wob_ttm"}).text + "°F"
#     # get the day and hour now
#     result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
#     # get the actual weather
#     result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text

#     # get the precipitation
#     result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
#     # get the % of humidity
#     result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
#     # extract the wind
#     result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

#     #extract image
#     image_url= str(soup.select( "#wob_tci")[0]).split()

#     result['img'] = "https:" + re.search(r'//\w+.\w+.\w+/\w+.+\w+', image_url[-1]).group()


#     return soup


def get_weather_data(city):

    BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"

    API_KEY = open(r"weatherpkg\openweatherapikey.txt", "r").read()

    url = BASE_URL + "appid=" + API_KEY + "&q=" + city

    response = requests.get(url).json()
    weather_data = {}
    if response['cod'] == '404':
        weather_data['invalid_city'] = " "

    else:
        # temperature
        temp_celsious = (response['main']['temp'])-273.15
        weather_data['temp_celsious'] = "%.2f" % temp_celsious + "°C"

        weather_data['temp_farenheit'] = "%.2f" % (
            temp_celsious * (9/5) + 32) + "°F"

        weather_data['desc'] = response['weather'][0]['description']
        weather_data['humidity'] = str(response['main']['humidity']) + "%"
        weather_data['wind'] = str(response['wind']['speed']) + "m/s"
        weather_data['datetime'] = dt.now().strftime("%d  %b %Y | %I:%M:%S %p")

    return weather_data

# print(get_weather_data("nairobi"))
