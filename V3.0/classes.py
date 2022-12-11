#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author: Vadym Tilihuzov
import random
#import time
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
            print("Generating remaining dots")
            count_to_generate = 20_020 - last_i
            for i in range(count_to_generate):
                based = random.choice(list(self.map))
                self.map.add(Dot(based.x + random.randrange(-100, 101), based.y + random.randrange(-100, 101), last_i+i))

    def generate_for_medoid(self):
        # generate 20 dots
        x:list = list(i for i in range(-5000, 5001))
        y:list = list(i for i in range(-5000, 5001))
        for i in range(20):
            a = random.choice(x)
            b = random.choice(y)
            x.remove(a)
            y.remove(b)
            self.map.add(Dot(float(a), float(b), i))
        # generate 5_000 dots
        for i in range(5_000):
            based = random.choice(list(self.map))
            self.map.add(Dot(based.x + random.randrange(-100, 101), based.y + random.randrange(-100, 101), i+20))
        # generate remaining dots if needed
        last_i = len(self.map)
        if last_i < 5_020:
            print("Generating remaining dots")
            count_to_generate = 5_020 - last_i
            for i in range(count_to_generate):
                based = random.choice(list(self.map))
                self.map.add(Dot(based.x + random.randrange(-100, 101), based.y + random.randrange(-100, 101), last_i+i))

    def print_all_dots(self):
        print([i.index for i in self.map])

    def generate_clusters(self):
        # generate clusters (for the first time)
        for index, i in enumerate(self.map):
            self.cluster.append(Cluster())
            self.cluster[index].head = i
            self.cluster[index].tail = i
            self.count_center(self.cluster[index])

    def generate_TD_distance(self):
        # making 2d array of distances between clusters (for the first time)
        for i in range(len(self.cluster)):
            self.TD_distance.append([])
            for j in range(len(self.cluster)):
                self.TD_distance[i].append(self.distance(self.cluster[i].center_x, self.cluster[i].center_y, self.cluster[j].center_x, self.cluster[j].center_y))
    
    def count_center(self, cluster:ClusterT):
        # count center of cluster
        count = 0
        x = 0
        y = 0
        current = cluster.head
        if current.next == None:
            cluster.center_x = current.x
            cluster.center_y = current.y
            return
        while current:
            count += 1
            x += current.x
            y += current.y
            current = current.next
        cluster.center_x = x / count
        cluster.center_y = y / count

    def count_center_for_medoid(self, cluster:ClusterT):
        # find center of cluster (medoid method)
        # based on center of mass i will find dot with the smallest distance to it
        # and it will be the center of cluster
        if cluster.head.next == None:
            cluster.center_x = cluster.head.x
            cluster.center_y = cluster.head.y
            return
        self.center = Dot(cluster.center_x, cluster.center_y, -1)
        min_distance = self.distance_dots(self.center, cluster.head)
        current = cluster.head
        while current:
            distance = self.distance_dots(self.center, current)
            if distance < min_distance:
                min_distance = distance
                cluster.center_x = current.x
                cluster.center_y = current.y
            current = current.next

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

    def centroid(self, k:int):
        """
        :param k: number of clusters
        """
        self.generate_clusters()
        self.generate_TD_distance()
        #startTime = time.time()
        while len(self.cluster) > k:
            # find min distance
            min_distance = self.TD_distance[0][1]
            min_i = 0
            min_j = 1
            for i in range(len(self.cluster)):
                for j in range(i+1, len(self.cluster)):
                    if self.TD_distance[i][j] < min_distance:
                        min_distance = self.TD_distance[i][j]
                        min_i = i
                        min_j = j
            # merge clusters
            self.cluster[min_i] = self.cluster[min_i].make_one_from_two_clusters(self.cluster[min_i], self.cluster[min_j])
            self.cluster.remove(self.cluster[min_j])
            # count center of new cluster
            self.count_center(self.cluster[min_i])
            # update TD_distance
            self.TD_distance.pop(min_j)
            for i in self.TD_distance:
                i.pop(min_j)
            for i in range(len(self.cluster)):
                if i != min_i:
                    self.TD_distance[min_i][i] = self.distance(self.cluster[min_i].center_x, self.cluster[min_i].center_y, self.cluster[i].center_x, self.cluster[i].center_y)
                    self.TD_distance[i][min_i] = self.TD_distance[min_i][i]
        
        #executionTime = (time.time() - startTime)
        #print('Execution time in seconds: ' + str(executionTime))
        # print statistics
        self.statistics(k)
        # print clusters
        self.picture_after(k, 'centroid')

    def medoid(self, k:int):
        """
        :param k: number of clusters
        """
        self.generate_clusters()
        self.generate_TD_distance()
        #startTime = time.time()
        while len(self.cluster) > k:
            # find min distance
            min_distance = self.TD_distance[0][1]
            min_i = 0
            min_j = 1
            for i in range(len(self.cluster)):
                for j in range(i+1, len(self.cluster)):
                    if self.TD_distance[i][j] < min_distance:
                        min_distance = self.TD_distance[i][j]
                        min_i = i
                        min_j = j
            # merge clusters
            self.cluster[min_i] = self.cluster[min_i].make_one_from_two_clusters(self.cluster[min_i], self.cluster[min_j])
            self.cluster.remove(self.cluster[min_j])
            # count center of new cluster
            self.count_center_for_medoid(self.cluster[min_i])
            # update TD_distance
            self.TD_distance.pop(min_j)
            for i in self.TD_distance:
                i.pop(min_j)
            for i in range(len(self.cluster)):
                if i != min_i:
                    self.TD_distance[min_i][i] = self.distance(self.cluster[min_i].center_x, self.cluster[min_i].center_y, self.cluster[i].center_x, self.cluster[i].center_y)
                    self.TD_distance[i][min_i] = self.TD_distance[min_i][i]
        #executionTime = (time.time() - startTime)
        #print('Execution time in seconds: ' + str(executionTime))
        # print statistics
        # self.statistics(k)
        # print clusters
        # self.picture_after(k, 'medoid')
            
    def picture_after(self, k:int, method:str='centroid'):
        import matplotlib.pyplot as plt
        #colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple', 'pink', 'brown', 'gray', 'olive', 'cyan']
        for i in range(k):
            x = []
            y = []
            current = self.cluster[i].head
            while current:
                x.append(current.x)
                y.append(current.y)
                current = current.next
            plt.scatter(x, y) # add all clusters
            plt.scatter(self.cluster[i].center_x, self.cluster[i].center_y, color='black') # add center of cluster
        plt.title(f'After clustering with {k} clusters')
        plt.set_xlabel(method) # add method
        plt.savefig(f'{method}_{k}.png')
        plt.show()

    def statistics(self, k:int):
        # find max distance from center in cluster
        # if max distance > 500: print('bad')
        # else: print('good') and count number of good clusters and bad clusters
        good = 0
        bad = 0
        for i in range(k):       
            max_distance = 0
            current = self.cluster[i].head
            while current:
                distance = self.distance(current.x, current.y, self.cluster[i].center_x, self.cluster[i].center_y)
                if distance > max_distance:
                    max_distance = distance
                current = current.next
            if max_distance > 500:
                bad += 1
            else:
                good += 1
        print(f'Good clusters: {good}, bad clusters: {bad}')


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
        self.center:DotT = None
        self.head = None
        self.tail = None
    
    def make_one_from_two_clusters(self, cluster1:ClusterT, cluster2:ClusterT) -> ClusterT:
        cluster1.tail.next = cluster2.head
        cluster1.tail = cluster2.tail
        return cluster1
