# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from weatherpkg.weather import get_current_weather, get_daily_weather
from climateaction.cckenya import region_data


class ActionCurrentWeatherForecast(Action):

    def name(self) -> Text:
        return "current_weather_forecast"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        city = tracker.get_slot("city")
        forecast = get_current_weather(city)

        dispatcher.utter_message(text = f"current weather is {forecast['symbolPhrase']}")
        dispatcher.utter_message(image = forecast['symbolimg'])
        dispatcher.utter_message(text = f"Feels like {forecast['feelsLikeTemp']}°C, with precipitaion of {forecast['precipProb']}% and humidity level of {forecast['relHumidity']}%")
       
        return []

class ActionDailyWeatherForecast(Action):

    def name(self) -> Text:
        return "daily_weather_forecast"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        city = tracker.get_slot("city")
        date = tracker.get_slot("date")
        daily_forecast = get_daily_weather(city, date)

        dispatcher.utter_message(text = f"Weather in {city} for {date} will be {daily_forecast['symbolphrase']}")
        dispatcher.utter_message(image = daily_forecast['symbolimg'])
        dispatcher.utter_message(text = f" will have a max temp of {daily_forecast['maxTemp']}°C, with precipitaion of {daily_forecast['precipAccum']}%")
       
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


        for img in reg_img:
            dispatcher.utter_message(image =img)

        dispatcher.utter_message(text= reg_preview)

        for art in reg_articles:
            dispatcher.utter_message(text =art)


        for vid in reg_videos:
            dispatcher.utter_message(text =vid)

        return []



  

# weather_forecast = ActionWeatherForecast()
# data = weather_forecast.weather_data("india")
# print(data)


