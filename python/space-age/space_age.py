class SpaceAge(object):
    def __init__(self, seconds: int):
        self.earth_year = 365.25
        self.earth_ratio = 86400

        self.seconds = seconds

        self.planet_ratio = {'Mercury': 0.2408467, "Venus": 0.61519726, "Earth": 1, "Mars": 1.8808158, \
            'Jupiter': 11.862615, 'Saturn': 29.447498, 'Uranus': 84.016846, 'Neptune': 164.79132}

    def __get_earth_years(self, ratio: float):
        return round(self.seconds / (self.earth_year * ratio * self.earth_ratio), 2)

    def on_mercury(self):
        return self.__get_earth_years(self.planet_ratio['Mercury'])

    def on_venus(self):
        return self.__get_earth_years(self.planet_ratio['Venus'])

    def on_earth(self):
        return self.__get_earth_years(self.planet_ratio['Earth'])

    def on_mars(self):
        return self.__get_earth_years(self.planet_ratio['Mars'])

    def on_jupiter(self):
        return self.__get_earth_years(self.planet_ratio['Jupiter'])

    def on_saturn(self):
        return self.__get_earth_years(self.planet_ratio['Saturn'])

    def on_uranus(self):
        return self.__get_earth_years(self.planet_ratio['Uranus'])

    def on_neptune(self):
        return self.__get_earth_years(self.planet_ratio['Neptune'])
