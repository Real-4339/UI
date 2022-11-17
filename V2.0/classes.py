import random
import math


class Map:
    def __init__(self) -> None:
        self.coordinates_that_can_be_used = [value for value in range(201)] # list of coordinates that can be used for cities
        self.width = 200 # width in km
        self.height = 200 # height in km
        self.cities = [] # list of cities
    
    def add_cities(self, city1, city2):
        self.cities.append(city1)
        self.cities.append(city2)
    
    def add_city(self, city):
        self.cities.append(city)
    
    def print_cities(self):
        for city1, city2, dis in self.cities:
            print(f"From city A: {city1.x, city1.y} to city B: {city2.x, city2.y} is {dis} km")

    def generate_coordinates(self) -> tuple:
        x = random.choice(self.coordinates_that_can_be_used) # x in km
        self.coordinates_that_can_be_used.remove(x)
        y = random.choice(self.coordinates_that_can_be_used) # y in km
        self.coordinates_that_can_be_used.remove(y)
        return (x, y)
    
    def greedy_answer(self):
        answer_vektor = [] # list of cities
        city1: City = self.cities[0] # copy of the first city
        city2 = city1 # city2 is the city that is the closest to city1
        answer_vektor.append(city1) # add city1 to the answer_vektor

        for a in range(len(self.cities)):
            min_distance = 32**2 

            for city in self.cities:
                if city not in answer_vektor:
                    dis = distance(city1.x, city1.y, city.x, city.y)
                    if dis < min_distance:
                        min_distance = dis
                        city2 = city
            answer_vektor.append(city2)
            city1 = city2
        
        answer_vektor.pop()

        return answer_vektor


class City:
    def __init__(self, index) -> None:
        self.index = index # index of city
        self.x = 0 # x coordinate of city
        self.y = 0 # y coordinate of city
    
    def __copy__(self) -> 'City':
        city = City(self.index)
        city.x = self.x
        city.y = self.y
        return city
    
    def __str__(self) -> str:
        return f"City {self.index} is at {self.x, self.y} km"


def distance(x1:int, y1:int, x2:int, y2:int) -> float:
        return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def generator() -> Map:
    map = Map()
    for i in range(20):
        city1 = City(i)
        city1.x, city1.y = map.generate_coordinates()

        # print(city1.x, city1.y, "coordinates")
        
        map.add_city(city1)
    
    return map