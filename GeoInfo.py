class GeoPosition:
    def __init__(self,latitude,longitude, radius):
        self.longitude = longitude
        self.latitude = latitude
        self.radius = radius


class VictimInfo:
    def __init__(self, position):
        """

        :param position: GeoPosition var
        """
        self.location = position


class VictimRegion:
    def __init__(self, position, populationCount):
        """

        :param position: GeoPosition var
        :param populationCount: int
        """
        self.location = position
        self.populationCount = populationCount


class VolunteersCenter:
    def __init__(self, position, numbers):
        """

        :param position: GeoPosition var
        :param numbers: int
        """
        self.location = position
        self.responderNumbers = numbers
