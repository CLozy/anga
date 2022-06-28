# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from weatherpkg.weather import get_weather_data
from climateaction.cckenya import region_data


class ActionWeatherForecast(Action):

    def name(self) -> Text:
        return "action_weather_forecast"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        city_slot_value = tracker.get_slot("city")
        forecast = get_weather_data(city_slot_value)

        if 'invalid_city' in forecast.keys() and  forecast['invalid_city'] == ' ': 
            dispatcher.utter_message(text="Please enter valid city name ")

        else:
            message = f"The current weather in {city_slot_value}  for {forecast['datetime']} displays {forecast['desc']}.\nTemperature: {forecast['temp_celsious']} | {forecast['temp_farenheit']}. \nHumidity: {forecast['humidity']}. \nWind: {forecast['wind']}"
            
            dispatcher.utter_message(text = "Okay, Looking at the sky :)")
            dispatcher.utter_message(text=message)
       

        return []


class ActionRegionClimate(Action):

    def name(self) -> Text:
        return "action_region_climate"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        region_slot_value = tracker.get_slot("region")
        reg_info = region_data(region_slot_value)

        reg_img = reg_info['reg_image']
        reg_preview = reg_info['preview']
        reg_articles = reg_info['articles']
        reg_videos = reg_info['videos']

        dispatcher.utter_message(image = reg_img)
        dispatcher.utter_message(text= reg_preview)

        for art in reg_articles:
            dispatcher.utter_message(text =art)


        for vid in reg_videos:
            dispatcher.utter_message(text =vid)

        return []



  

# weather_forecast = ActionWeatherForecast()
# data = weather_forecast.weather_data("india")
# print(data)


