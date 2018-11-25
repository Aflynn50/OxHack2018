import Demographics as dem
import heapq
import math


class ManageSit:
    def __init__(self, victims, centers, victimsRegions, usingTestData):
        if usingTestData:
            self.affectedRegions = victimsRegions
        else:
            self.affectedRegions = dem.getVictimRegion(victims)
        self.centers = centers


    def addCenter(self, center):
        self.centers.append(center)

    def addAff(self, aff):
        self.affectedRegions.append(aff)

    @staticmethod
    def computeDistance(pos1, pos2):
        R = 6371
        ph1 = math.radians(pos1.latitude)
        ph2 = math.radians(pos2.latitude)
        deltph = math.radians(pos2.latitude - pos1.latitude)
        deltlam = math.radians(pos2.longitude - pos1.longitude)
        a = math.sin(deltph / 2) * math.sin(deltph / 2) + \
            math.cos(ph1) * math.cos(ph2) * \
            math.sin(deltlam / 2) * math.sin(deltlam / 2)
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return R * c

    def dispatch(self):
        deltaDist = []
        for idxAff, affectedRegion in enumerate(self.affectedRegions):
            for idxCent, center in enumerate(self.centers):
                deltaDist.append((self.computeDistance(affectedRegion.location, center.location),
                                  idxAff,
                                  idxCent))
        heapq.heapify(deltaDist)

        seenAffected = set()
        seenCenters = set()
        assigned = []
        while deltaDist:
            dist, aff, cent = heapq.heappop(deltaDist)
            if (aff in seenAffected) or (cent in seenCenters):
                continue

            affPopCount = self.affectedRegions[aff].populationCount
            centResNum = self.centers[cent].responderNumbers

            if affPopCount * 0.1 >= centResNum:
                seenCenters.add(cent)
                self.affectedRegions[aff].populationCount -= centResNum * 10
                numAssigned = centResNum
            else:
                seenAffected.add(aff)
                self.centers[cent].responderNumbers -= math.ceil(affPopCount * 0.1)
                if self.centers[cent].responderNumbers == 0:
                    seenCenters.add(cent)
                numAssigned = math.ceil(affPopCount * 0.1)

            assigned.append((self.affectedRegions[aff].location,
                             self.centers[cent].location,
                             numAssigned))

        newAff = []
        for idxAff, affectedRegion in enumerate(self.affectedRegions):
            if idxAff not in seenAffected:
                newAff.append(affectedRegion)
        self.affectedRegions = newAff

        newCenters = []
        for idxCent, center in enumerate(self.centers):
            if idxCent not in seenCenters:
                newCenters.append(center)
        self.centers = newCenters

        return assigned




