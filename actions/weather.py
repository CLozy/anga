
import requests
import re
from bs4 import BeautifulSoup

def weather_data(city):

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

    #extract image
    image_url= str(soup.select( "#wob_tci")[0]).split()

    result['img'] = "https:" + re.search(r'//\w+.\w+.\w+/\w+.+\w+', image_url[-1]).group() 
    
    
    return result


def get_weather_data(city):
    data = weather_data(city)
    return data