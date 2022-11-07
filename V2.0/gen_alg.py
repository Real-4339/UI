import random
import classes


def fitnes(array: list) -> int:
    return sum(classes.distance(array[a].x, array[a].y, array[a+1].x, array[a+1].y) for a in range(len(array)-1))  # type: ignore

def choose_1(array: list, array_of_fitnes: list) -> list:
    # choose function based on fitnes
    pass

def genetics_algorithm():
    map = classes.generator()
    answer = map.answer() # answer vektor of cities: list
    array = [] # list of vectors
    array_of_fitnes = [] # list of fitnes

    # first generation
    for a in range(20):
        arr = answer[:]
        random.shuffle(arr)
        if arr not in array:
            array_of_fitnes.append(fitnes(arr))
            array.append(arr)
    
    # choose function based on fitnes
    
    # crossover
    # mutation
    
    # cycle through generations
    # while new_map.answer() != answer:
    #     new_map = classes.generator()
    #     if new_map.answer() < answer:
    #         answer = new_map.answer()
    #         old_map = new_map
    