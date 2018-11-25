import os
import sys
sys.path.append(os.getcwd())
from TwitterSearch import *
import requests
from GeoInfo import VictimInfo, GeoPosition 

class SearchFrame:
    def __init__(self):
        self.longitude = 51.7555  #Specify a box of size (x * divsize) * (y * divsize) with top left corner in pos long, lat
        self.latitude = 0.0
        self.x = 1
        self.y = 1
        self.diameter = 10 #diameter of search circles in box, in miles 


def getVictims():
    frame = SearchFrame()
    geolocations = [[[] for i in range(0,frame.x)] for j in range(0,frame.y)]
    for i in range(0,frame.x):
        for j in range(0,frame.y):
            tso = TwitterSearchOrder()
            tso.set_keywords(["tornado", "EF", "hail", "storm", "damage", "injur", "kill", "wind", "thunder", "water", "flood", "rain", "wound", "loss", "help", "save"], or_operator=True)
            tso.set_geocode(float(frame.longitude + (i*frame.diameter)), float(frame.latitude + (j*frame.diameter)), int(frame.diameter/2))
            searchResults = TwitterSearch(consumer_key="eoe5TmgDTsmI0E2NpSrt7KPfg",
                                               consumer_secret="onNO7vobeUw1piKWfmXQJwmpMKrQbzRWTeXFjKo6nZwipCPJ3r",
                                               access_token="2491643690-UVYiYfoc3VXyQ4dc5B2VcSCMTU0hsl0www8dB7n",
                                               access_token_secret="g8RmQzuyIA0vgxfCgTcMsSshbWYGmhmKfIO3320TQ6isY")
    for tweet in searchResults.search_tweets_iterable(tso):
        #print('@%s tweeted: %s' % (tweet['user']['screen_name'],tweet['text']))
        geolocations[i][j].append(tweet)
    
    geolocations = azureApi(geolocations)

    returnlist = []

    for i in range(0,frame.x):
        for j in range(0,frame.y):
            for tweet in geolocations[i][j]:
                returnlist.append(VictimInfo(GeoPosition(frame.longitude + (i*frame.diameter), frame.latitude + (j*frame.diameter), int(frame.diameter/2))))
    
    return returnlist


def azureApi(geolocs):
    azurekey = "29c7bf1a559d4d2e8e83db07740b33eb"
    text_analytics_base_url = "https://uksouth.api.cognitive.microsoft.com/text/analytics/v2.0/"
    sentiment_api_url = text_analytics_base_url + "sentiment"
    values = []
    for x in geolocs:
        for y in x:
            for z in y:
                values.append({'id': z['id'], 'text': z['text'], 'language': 'en'})
    
    documents = { 'documents' : values}

    headers   = {"Ocp-Apim-Subscription-Key": azurekey}
    response  = requests.post(sentiment_api_url, headers=headers, json=documents)
    sentiments = response.json()
    threshold = 0.25
    unhappytweets = [x['id'] for x in sentiments['documents'] if x['score'] < threshold]
    
    for x in geolocs:
        for y in x:
            for z in y:
                if z['id'] in unhappytweets:
                    y.remove(z)
    return geolocs

