from newsapi import NewsApiClient

API_KEY = open("climateaction\\newsapikey.txt", "r").read()

newsapi = NewsApiClient(API_KEY)


def coastal_region(region):
    news_headlines = newsapi.get_top_headlines(
        q=f'how {region} region of kenya is affected by climate change', language='en')
    return news_headlines
