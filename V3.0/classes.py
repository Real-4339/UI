#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Vadym Tilihuzov
import random


class Map:

    coordinates_x: set = set()
    coordinates_y: set = set()

    def __init__(self):
        self.width = 10_000 # from -5_000 to 5_000
        self.height = 10_000 # from -5_000 to 5_000
        self.map = [] # array of dots
        self.generate()

    def generate(self):
        x:list = list(i for i in range(-5000, 5001))
        y:list = list(i for i in range(-5000, 5001))
        for i in range(20):
            a = random.choice(x)
            b = random.choice(y)
            self.coordinates_x.add(float(a))
            self.coordinates_y.add(float(b))
            x.remove(a)
            y.remove(b)
            self.map.append(Dot(float(a), float(b), i))
    
    def picture(self):
        import matplotlib.pyplot as plt
        x = [i.x for i in self.map]
        y = [i.y for i in self.map]
        plt.scatter(x, y)
        plt.show()


class Dot:
    def __init__(self, x:float , y:float, index:int) -> None:
        self.x: float = x
        self.y: float = y
        self.index = index


class Cluster:
    ...


