from geopy.geocoders import Nominatim
from GeoInfo import GeoPosition,VictimInfo,VictimRegion
import wptools
from wikidata.client import Client

class RegionCount:
    def __init__(self,region,reportCount):
        self.region = region
        self.reportCount = reportCount

def getVictimRegion(victims):
    regionCounts = {}
    geolocator = Nominatim(user_agent="oxHack")
    for victim in victims:
        coordsString = str(victim.location.longitude) + ", "+str(victim.location.latitude)
        location = geolocator.reverse(coordsString)
        if location.address in regionCounts:
            regionCounts[location.address].reportCount += 1
        else:
            addressParts = location.address.split(", ")
            population = -1
            for part in addressParts:
                if population>0:
                    break
                wikipage = None
                wikidataPage = None
                try:
                    wikipage = wptools.page(part).get_parse()
                    client = Client()
                    wikidataPage = client.get(wikipage.data['wikibase'],load=True)
                    population = wikidataPage.data['claims']['P1082'][0]['mainsnak']['datavalue']['value']['amount']
                    population = int(population[1:])
                except:
                    pass
                i = 0
            if population>0:
                thisRegion = VictimRegion(victim.location,population)
                thisRegionCount = RegionCount(thisRegion,1)
                regionCounts[location.address] = RegionCount(thisRegion, 1)



    finalRegions = []
    for countedRegionName in regionCounts:
        thisRegionCount = regionCounts[countedRegionName]
        if thisRegionCount.reportCount / thisRegionCount.region.populationCount > 0.05:
            finalRegions.append(thisRegionCount.region)
    return finalRegions