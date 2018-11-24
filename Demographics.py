#from geopy.geocoders import Nominatim
from GeoInfo import GeoPosition,VictimInfo,VictimRegion
import wptools
from wikidata.client import Client
import reverse_geocoder as rg

class RegionCount:
    def __init__(self,region,reportCount):
        self.region = region
        self.reportCount = reportCount

def getVictimRegion(victims):
    allCoords = []
    for victim in victims:
        allCoords.append( (victim.location.longitude,victim.location.latitude) )
    regionCounts = {}

    allLocations = rg.search(allCoords)

    for location in allLocations:
        locationAddress = location['name']+", "+location['admin1']+", "+location['admin2']
        if locationAddress in regionCounts:
            regionCounts[locationAddress].reportCount += 1
        else:
            addressParts = locationAddress.split(", ")
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
                regionCounts[locationAddress] = thisRegionCount
            else:
                longituteFloat = float(location['lon'])
                latitudeFloat = float(location['lat'])
                key = str(int(longituteFloat*4.0))+", "+str(int(latitudeFloat*4.0))
                if key in regionCounts:
                    regionCounts[key].reportCount += 1
                else:
                    thisRegionCount = RegionCount(thisRegion, 1)
                    regionCounts[key] = thisRegionCount


    finalRegions = []
    for countedRegionName in regionCounts:
        thisRegionCount = regionCounts[countedRegionName]
        if thisRegionCount.reportCount / thisRegionCount.region.populationCount > 0.5:
            finalRegions.append(thisRegionCount.region)
    return finalRegions