#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Vadym Tilihuzov
import random
import numpy as np
from typing import TypeVar

DotT = TypeVar("DotT", bound="Dot")
ClusterT = TypeVar("ClusterT", bound="Cluster")

class Map:

    TD_distance: list = list(list()) # two-dimensional distance TD
    cluster: list = list() # array of clusters

    def __init__(self):
        self.width = 10_000 # from -5_000 to 5_000
        self.height = 10_000 # from -5_000 to 5_000
        self.map:set = set() # array of dots
        self.generate()

    def generate(self):
        # generate 20 dots
        x:list = list(i for i in range(-5000, 5001))
        y:list = list(i for i in range(-5000, 5001))
        for i in range(20):
            a = random.choice(x)
            b = random.choice(y)
            x.remove(a)
            y.remove(b)
            self.map.add(Dot(float(a), float(b), i))
        # generate 20_000 dots
        for i in range(20_000):
            based = random.choice(list(self.map))
            self.map.add(Dot(based.x + random.randrange(-100, 101), based.y + random.randrange(-100, 101), i+20))
        # generate remaining dots if needed
        last_i = len(self.map)
        if last_i < 20_020:
            count_to_generate = 20_020 - last_i
            for i in range(count_to_generate):
                based = random.choice(list(self.map))
                self.map.add(Dot(based.x + random.randrange(-100, 101), based.y + random.randrange(-100, 101), last_i+i))

    def generate_clusters(self):
        # generate clusters (for the first time)
        for i in self.map:
            self.cluster.append(Cluster())
            self.cluster[i.index].head = i
            self.cluster[i.index].tail = i

    def generate_TD_distance(self):
        # making 2d array of distances between clusters (for the first time)
        for i in range(len(self.cluster)):
            self.TD_distance.append([])
            for j in range(len(self.cluster)):
                self.TD_distance[i].append(self.distance_dots(self.cluster[i].head, self.cluster[j].head))

    def print_TD_distance(self):
        for i in self.TD_distance:
            print(i)
    
    def distance_dots(self, dot1:DotT, dot2:DotT):
        return ((dot2.x - dot1.x)**2 + (dot2.y - dot1.y)**2)**0.5
    
    def distance(self, center_x1:float, center_y1:float, center_x2:float, center_y2:float):
        return ((center_x2 - center_x1)**2 + (center_y2 - center_y1)**2)**0.5

    def picture_before(self):
        import matplotlib.pyplot as plt
        x = [i.x for i in self.map]
        y = [i.y for i in self.map]
        plt.scatter(x, y)
        plt.title('Before clustering')
        plt.show()

    # remake this function
    def centroid(self, k:int):
        """
        :param k: number of clusters
        """
        self.generate_clusters()
        self.generate_TD_distance()
        # centroids = []
        # choices = np.random.choice(self.map, k, replace=False)
        # for i in choices:
        #     centroids.append(i)
        
        
    def picture_after(self):
        pass


class Dot:
    def __init__(self, x:float , y:float, index:int, next=None) -> None:
        self.x: float = x
        self.y: float = y
        self.index = index
        self.next = next
    
    def __hash__(self):
        return hash((self.x, self.y))


class Cluster:
    def __init__(self) -> None:
        self.center_x:float = 0
        self.center_y:float = 0
        self.head = None
        self.tail = None
    
    def make_one_from_two_clusters(self, cluster1:ClusterT, cluster2:ClusterT) -> ClusterT:
        cluster1.tail.next = cluster2.head
        cluster1.tail = cluster2.tail
        return cluster1