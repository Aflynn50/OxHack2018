from DispatchStrategy import ManageSit
import Demographics
from GeoInfo import GeoPosition,VictimInfo,VictimRegion


victims = []
for i in range(10000):
    victimPos0 = GeoPosition(45, 28, 1)
    victim0 = VictimInfo(victimPos0)
    victims.append(victim0)


for i in range(10000):
    victimPos0 = GeoPosition(51.5074, 0.1278, 1)
    victim0 = VictimInfo(victimPos0)
    victims.append(victim0)

victimRegions = Demographics.getVictimRegion(victims)
print(len(victimRegions))