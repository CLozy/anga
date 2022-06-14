# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []



from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import requests
from bs4 import BeautifulSoup

class ActionWeatherForecast(Action):

    def name(self) -> Text:
        return "action_weather_forecast"


    def weather_data(self, city):

        USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.63 Safari/537.36"
        LANGUAGE = "en-KE,en;q=0.5"

        URL = "https://www.google.com/search?lr=lang_en&ie=UTF-8&q=weather"
        URL+= city

        session = requests.Session()
        session.headers['User-Agent'] = USER_AGENT
        session.headers['Accept-Language'] = LANGUAGE
        session.headers['Content-Language'] = LANGUAGE
        html = session.get(URL)
        # create a new soup
        soup = BeautifulSoup(html.text, "html.parser")
        
         # store all results on this dictionary
        result = {}
        # extract region
        result['region'] = soup.find("div", attrs={"id": "wob_loc"}).text 

        #get temp in celsius and farenheit

        result['temp_now_c'] = soup.find("span", attrs={"id": "wob_tm"}).text + "°C"
        result['temp_now_f'] = soup.find("span", attrs={"id": "wob_ttm"}).text + "°F"
        # get the day and hour now
        result['dayhour'] = soup.find("div", attrs={"id": "wob_dts"}).text
        # get the actual weather
        result['weather_now'] = soup.find("span", attrs={"id": "wob_dc"}).text
        
        # get the precipitation
        result['precipitation'] = soup.find("span", attrs={"id": "wob_pp"}).text
        # get the % of humidity
        result['humidity'] = soup.find("span", attrs={"id": "wob_hm"}).text
        # extract the wind
        result['wind'] = soup.find("span", attrs={"id": "wob_ws"}).text

        # result['image_url'] = soup.find("img", attrs={"id" : "wob_tci"}).text
        image_url= str(soup.select( "#wob_tci")[0]).split()
        result['img'] = image_url[-1]
       
       
        return result

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []





  

weather_forecast = ActionWeatherForecast()
data = weather_forecast.weather_data("nyeri")
print(data)


