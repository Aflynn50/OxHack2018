from DispatchStrategy import ManageSit
import VictumInfo as vi
from GeoInfo import VolunteersCenter, GeoPosition
if __name__ == '__main__':

    temp = vi.getUpdateTweets()

    victims = vi.getVictims()

    centers = []
    centers.append(VolunteersCenter(GeoPosition(45.4, 21, 4), 1))
    centers.append(VolunteersCenter(GeoPosition(46, 24, 4), 1))
    centers.append(VolunteersCenter(GeoPosition(44.5, 28, 4), 1))
    centers.append(VolunteersCenter(GeoPosition(47, 27.5, 4), 1))
    centers.append(VolunteersCenter(GeoPosition(44.3, 28, 4), 1))

    disp = ManageSit(victims, centers)
    assocs = disp.dispatch()
    print(assocs)


    # victimRegions = []
    # centers = []
    #
    #
    # victimRegions.append(VictimInfo(GeoPosition(44, 20, 4)))
    # victimRegions.append(VictimInfo(GeoPosition(46, 23, 4)))
    # victimRegions.append(VictimInfo(GeoPosition(44, 28, 4)))
    # victimRegions.append(VictimInfo(GeoPosition(47, 27, 4)))
    # victimRegions.append(VictimInfo(GeoPosition(45, 25, 4)))
    #

