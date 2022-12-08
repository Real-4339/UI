#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Vadym Tilihuzov
import random
import numpy as np
from typing import TypeVar

DotT = TypeVar("DotT", bound="Dot")

class Map:

    coordinates_x: set = set()
    coordinates_y: set = set()
    TD_distance: list = list(list()) # two-dimensional distance TD

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

    def generate_TD_distance(self):
        for i in range(len(self.map)):
            self.TD_distance.append([])
            for j in range(len(self.map)):
                self.TD_distance[i].append(self.distance(self.map[i], self.map[j]))

    def print_TD_distance(self):
        for i in self.TD_distance:
            print(i)
    
    def distance(self, dot1:DotT, dot2:DotT):
        return ((dot2.x - dot1.x)**2 + (dot2.y - dot1.y)**2)**0.5
    
    def picture_before(self):
        import matplotlib.pyplot as plt
        x = [i.x for i in self.map]
        y = [i.y for i in self.map]
        for i in range(len(x)):
            plt.scatter(x[i], y[i])
        plt.title('Before clustering')
        plt.show()

    def centroid(self, k:int):
        """
        :param k: number of clusters
        """
        self.generate_TD_distance()
        centroids = []
        choices = np.random.choice(self.map, k, replace=False)
        for i in choices:
            centroids.append(i)
        
        
    def picture_after(self):
        pass


class Dot:
    def __init__(self, x:float , y:float, index:int) -> None:
        self.x: float = x
        self.y: float = y
        self.index = index


class Cluster:
    def __init__(self) -> None:
        self.center = 0
        self.dots = []


