from TwitterSearch import *

class GeoPosition:
    def __init__(self):
        self.longitude = 0
        self.latitude = 0
        self.radius = 0


class VictimInfo:
    def __init__(self):
        self.location = "51.7555,0,100mi"
        self.tso = TwitterSearchOrder()
        self.tso.set_keywords(["help"])
        self.tso.set_geocode(51.7555,0.0,100)
        self.searchResults = TwitterSearch(consumer_key="eoe5TmgDTsmI0E2NpSrt7KPfg",
                                           consumer_secret="onNO7vobeUw1piKWfmXQJwmpMKrQbzRWTeXFjKo6nZwipCPJ3r",
                                           access_token="2491643690-UVYiYfoc3VXyQ4dc5B2VcSCMTU0hsl0www8dB7n",
                                           access_token_secret="g8RmQzuyIA0vgxfCgTcMsSshbWYGmhmKfIO3320TQ6isY")
        for tweet in self.searchResults.search_tweets_iterable(self.tso):
            print('@%s tweeted: %s' % (tweet['user']['screen_name'],tweet['text']))

v = VictimInfo()

