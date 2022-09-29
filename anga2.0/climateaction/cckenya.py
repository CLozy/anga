import json
from newsapi import NewsApiClient

API_KEY = open("climateaction/key.txt", "r").read()

newsapi = NewsApiClient(API_KEY)


def region_data(region):
    with open("climateaction/climatedata.json", "r") as file:
        data = json.load(file)
    
    reg_info = {}
    for reg in data['kenya']:
        if reg == region.lower():
            reg_data = data['kenya'][reg]
            reg_info['reg_image'] = reg_data['image']
            reg_info['preview'] = reg_data['preview']
            reg_info['articles'] = reg_data['articles']
            reg_info['videos'] = reg_data['videos']
    return reg_info

# print(region_data("coast"))