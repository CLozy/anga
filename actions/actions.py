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

from weatherpkg.weather import get_weather_data


class ActionWeatherForecast(Action):

    def name(self) -> Text:
        return "action_weather_forecast"


    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:


        city_slot_value = tracker.get_slot("city")
        forecast = get_weather_data(city_slot_value)

        if forecast['invalid_city'] == ' ':
            dispatcher.utter_message(text="Please enter valid city name ")

        else:
            message = f"The current weather in {city_slot_value}  for {forecast['datetime']} displays {forecast['weather_now']}.\nTemperature: {forecast['temp_celsious']} | {forecast['temp_farenheit']}. \nHumidity: {forecast['humidity']}. \nWind: {forecast['wind']}"
            
            dispatcher.utter_message(text = "Okay, Looking at the sky :)")
            dispatcher.utter_message(text=message)
       

        return []

    



  

# weather_forecast = ActionWeatherForecast()
# data = weather_forecast.weather_data("india")
# print(data)


