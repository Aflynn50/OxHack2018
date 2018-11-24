from DispatchStrategy import ManageSit
from GeoInfo import GeoPosition, VictimRegion, VolunteersCenter


victimRegions = []
centers = []


victimRegions.append(VictimRegion(GeoPosition(44, 20, 4), 100))
victimRegions.append(VictimRegion(GeoPosition(46, 23, 4), 10232))
victimRegions.append(VictimRegion(GeoPosition(44, 28, 4), 102))
victimRegions.append(VictimRegion(GeoPosition(47, 27, 4), 1))
victimRegions.append(VictimRegion(GeoPosition(45, 25, 4), 10223122))

centers.append(VolunteersCenter(GeoPosition(45.4, 21, 4), 100))
centers.append(VolunteersCenter(GeoPosition(46, 24, 4), 10232))
centers.append(VolunteersCenter(GeoPosition(44.5, 28, 4), 10232))
centers.append(VolunteersCenter(GeoPosition(47, 27.5, 4), 10232))
centers.append(VolunteersCenter(GeoPosition(44.3, 28, 4), 10232))

disp = ManageSit(victimRegions, centers)
assocs = disp.dispatch()
print(assocs)

