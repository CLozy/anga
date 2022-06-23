import json
from newsapi import NewsApiClient

API_KEY = open("climateaction\\newsapikey.txt", "r").read()

newsapi = NewsApiClient(API_KEY)


def region_data(region):
    with open("climateaction\climatedata.json", "r") as file:
        data = json.load(file)
    
    for reg in data['kenya']:
        if reg == region:
            reg_data = data['kenya'][reg]
            articles = reg_data['articles']
            videos = reg_data['videos']

    
    return articles ,videos

# print(region_data("coast"))