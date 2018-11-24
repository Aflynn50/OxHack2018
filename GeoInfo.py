class GeoPosition:
    def __init__(self):
        self.longitude = 0
        self.latitude = 0
        self.radius = 0


class VictimInfo:
    def __init__(self):
        self.location = GeoPosition()


class VictimRegion:
    def __init__(self):
        self.location = GeoPosition
        self.populationCount = 0