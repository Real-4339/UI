import random
import math


class Map:
    def __init__(self) -> None:
        self.width = 200 # width in km
        self.height = 200 # height in km
        self.cities = [] # list of cities   

    def distance(self, x1:int, y1:int, x2:int, y2:int) -> float:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    def add_cities(self, city1, city2, distance):
        self.cities.append((city1, city2, distance))
    
    def print_cities(self):
        for city1, city2, dis in self.cities:
            print(f"From city A: {city1.x, city1.y} to city B: {city2.x, city2.y} is {dis} km")


class City:
    def __init__(self) -> None:
        self.x = random.randrange(0, 200) # x in km
        self.y = random.randrange(0, 200) # y in km


def generator() -> Map:
    map = Map()
    for i in range(20):
        city1 = City()
        city2 = City()
        map.add_cities(city1, city2, map.distance(city1.x, city1.y, city2.x, city2.y))
    
    return map