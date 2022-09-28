
import requests
import pandas as pd
import json
import os
import re
from bs4 import BeautifulSoup
from dotenv import load_dotenv

from datetime import datetime as dt


# params = {
#     "user": "clozymwangs",
#     "password": "Yd9DchqMli5x"
# }

# get_token = requests.post(url = 'https://pfa.foreca.com/authorize/token?', params=params)
# token = get_token.json()
# print(token)

def get_symbols(symbol):
    with open("weatherpkg/weathersymbols.json", "r") as file:
        symbols = json.load(file)
    
    for code in symbols['codes']:
        if symbol == code['symbol']:
            symbol_code = code
    weather_symbol_code = symbol_code

    return weather_symbol_code

    


def get_city_id(city):

    load_dotenv()

    api_key = os.getenv('FORECA_API_KEY')

    headers = {
        "Authorization" : f"Bearer {api_key}"
    }

    location_response = requests.get(url = f'https://pfa.foreca.com/api/v1/location/search/{city}?lang=en', headers=headers)
   
    location = location_response.json()


    city_id = location['locations'][0]['id']


    return city_id, headers


def get_current_weather(city):

    # city_lon = location['locations'][0]['lon']
    city_id, headers = get_city_id(city)

    current_weather_response = requests.get(url = f"https://pfa.foreca.com/api/v1/current/{city_id}", headers=headers) 
    current_weather = current_weather_response.json()

    symbol_codes = get_symbols(current_weather['current']['symbol'])

    current_weather_forecast = current_weather['current']
    current_weather_forecast['symbolimg'] = symbol_codes['img']

    return current_weather_forecast

def get_daily_weather(city, date):

    city_id, headers = get_city_id(city)

    daily_weather_response = requests.get(url = f"https://pfa.foreca.com/api/v1/forecast/daily/{city_id}", headers=headers)
    daily_weather = daily_weather_response.json()

    for forecast in daily_weather['forecast']:
        forecast['date_name'] = pd.Timestamp(forecast['date']).day_name().lower()
    
    if date.lower() == "tomorrow":
        daily_weather_forecast = daily_weather['forecast'][1]
        daily_weather_forecast['date_name'] = "tomorrow"

    for forecast in daily_weather['forecast']:
        if date.lower() == forecast['date_name']:
            daily_forecast = forecast
    daily_weather_forecast = daily_forecast

    symbol_codes = get_symbols(daily_weather_forecast['symbol'])
    daily_weather_forecast['symbolphrase']= symbol_codes['phrase']
    daily_weather_forecast['symbolimg']= symbol_codes['img']
    return daily_weather_forecast


# print(get_current_weather("london"))
# print("------------------")
# print(get_daily_weather("london","tuesday"))
# print(get_daily_weather("london", "tomorrow"))

