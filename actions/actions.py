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
from rasa_sdk.events import SlotSet

from . import weather


class ActionWeatherForecast(Action):

    def name(self) -> Text:
        return "action_weather_forecast"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        city_slot_value = tracker.get_slot("city")
        forecast = weather.get_weather_data(city_slot_value)

        message = f"The current weather in {forecast['region']} is {forecast['weather_now']}.\nTemperature: {forecast['temp_now_c']} | {forecast['temp_now_f']}.\n Precipitation: {forecast['precipitation']}. \nHumidity: {forecast['humidity']}. \nWind: {forecast['wind']}"

        dispatcher.utter_message(text=message)
       

        return []

    



  

# weather_forecast = ActionWeatherForecast()
# data = weather_forecast.weather_data("india")
# print(data)


