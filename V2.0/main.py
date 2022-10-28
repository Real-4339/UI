import random
import math


class Map:
    def __init__(self) -> None:
        self.width = 200 # width in km
        self.height = 200 # height in km
    
    def distance(self, x1, y1, x2, y2):
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


class Node:
    def __init__(self):
        self.x = random.randrange(0, 200) # x in km
        self.y = random.randrange(0, 200) # y in km


def start():
    ...