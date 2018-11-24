from TwitterSearch import *

class GeoPosition:
    def __init__(self):
        self.longitude = 51.7555  #Specify a box of size (x * divsize) * (y * divsize) with top left corner in pos long, lat
        self.latitude = 0.0
        self.x = 3
        self.y = 3
        self.diameter = 10 #diameter of search circles in box, in miles


class VictimInfo:
    def __init__(self):
        self.geoPos = GeoPosition()
        geolocations = [[0 for i in range(0,self.geoPos.x)] for j in range(0,self.geoPos.y)]
        for i in range(0,self.geoPos.x):
            for j in range(0,self.geoPos.y):
                self.tso = TwitterSearchOrder()
                self.tso.set_keywords(["help"])
                self.tso.set_geocode(float(self.geoPos.longitude + (i*self.geoPos.diameter)), float(self.geoPos.latitude + (j*self.geoPos.diameter)), int(self.geoPos.diameter/2))
                self.searchResults = TwitterSearch(consumer_key="eoe5TmgDTsmI0E2NpSrt7KPfg",
                                                   consumer_secret="onNO7vobeUw1piKWfmXQJwmpMKrQbzRWTeXFjKo6nZwipCPJ3r",
                                                   access_token="2491643690-UVYiYfoc3VXyQ4dc5B2VcSCMTU0hsl0www8dB7n",
                                                   access_token_secret="g8RmQzuyIA0vgxfCgTcMsSshbWYGmhmKfIO3320TQ6isY")
        for tweet in self.searchResults.search_tweets_iterable(self.tso):
            #print('@%s tweeted: %s' % (tweet['user']['screen_name'],tweet['text']))
            geolocations[i][j] += 1
        print(geolocations)

v = VictimInfo()

