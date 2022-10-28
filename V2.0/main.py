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


class Node:
    def __init__(self) -> None:
        self.x = random.randrange(0, 200) # x in km
        self.y = random.randrange(0, 200) # y in km


def start():
    ...