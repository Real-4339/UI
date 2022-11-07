import random
import classes


def fitnes(array: list) -> int:
    return sum(classes.distance(array[a].x, array[a].y, array[a+1].x, array[a+1].y) for a in range(len(array)-1))  # type: ignore

def new_permutation(array: list[list[classes.City]]) -> list[list[classes.City], list[int]]:  
    permutations: list[list[classes.City]] = [] # list of couple vectors
    restrictions: list[int] = [] # list of indexes of vectors that are already in permutations
    couple1 = 0
    couple2 = 0

    for a in range(len(array)):
        if couple2 == array[a]:
            continue
        
        if random.random() <= 0.6:
            couple1 = array[a]
        else:
            continue

        for i, b in enumerate(array):
            if b != couple1:
                if ( a not in restrictions and i not in restrictions ) and random.random() <= 0.6:
                    couple2 = b
                    
                    restrictions.append(a)
                    restrictions.append(i)
                    permutations.append(couple1)
                    permutations.append(couple2)

                    break
    
    for a in array:
        print([c.index for c in a])
    print("permutations", len(permutations))
    for a in permutations:
        print([c.index for c in a])

    return [permutations, restrictions]  # type: ignore

def crossover(array: list[list[classes.City]]) -> list[list[classes.City]]:
    # choose two vectors
    permutation, indexes = new_permutation(array) # list of cities that need to be csossed
    # choose n-1 cities in first vector
    # add other using order from second vector
    index_a_1 = 0
    index_a_2 = 0
    index_b_1 = 0
    index_b_2 = 0
    new_generation = []

    # put not changed vectors into new generation
    # for i, a in enumerate(array):
    #     if a not in permutation:
    #         print("not in permutation")
    #         indexes.append(i)
    
    # for r in array:
    #     print([c.index for c in r])
    # print("diff")
    # for r in permutation:
    #     print([c.index for c in r])
    # print(indexes)

    # put changed vectors into new generation
    for a, b in [permutation[i:i+2] for i in range(0, len(permutation), 2)]:
        diff_1 = 0
        diff_2 = 0
        
        while diff_1 == 0 or diff_1 == len(a)-1:
            index_a_1 = random.randint(0, len(a)-1)
            index_a_2 = random.randint(0, len(a)-1)
            diff_1 = abs(index_a_1 - index_a_2)

        while diff_2 == 0 or diff_2 == len(b)-1:
            index_b_1 = random.randint(0, len(b)-1)
            index_b_2 = random.randint(0, len(b)-1)
            diff_2 = abs(index_b_1 - index_b_2)

        if index_a_1 > index_a_2:
            for v in a[index_a_2:index_a_1+1]:
                ...#print(v, "1>2")
        else:
            for v in a[index_a_1:index_a_2+1]:
                ...#print(v, "2>1")

    return new_generation

def choose_roulette(array_of_fitnes: list) -> int:
    # choose function (roulette)
    S = int(sum(cc for cc in array_of_fitnes))
    r = random.randint(0, S-1)
    max = 0
    index = -1

    for ind, a in enumerate(array_of_fitnes):
        max += a
        if max > r:
            index = ind
            break
    
    return index

def choose_order(array_of_fitnes: list) -> int:
    array_of_fitnes.sort()
    index = random.choice(array_of_fitnes)
    return array_of_fitnes.index(index)

def println(array: list) -> None: 
    print(len(array), ':lenght')
    for i, a in enumerate(array):
        print("new", i)
        for cc in a:
            print(cc)

def printls(array: list) -> None:
    print('output')
    for a in array:
        print(a)

def genetics_algorithm():
    map = classes.generator()
    answer = map.answer() # answer vektor of cities: list
    parrent_array = [] # list of vectors
    array_of_fitnes = [] # list of fitnes

    # first generation
    for a in range(20):
        arr = answer[:]
        random.shuffle(arr)
        if arr not in parrent_array:
            array_of_fitnes.append(fitnes(arr))
            parrent_array.append(arr)
        # else !? -------------------------------------------->
    
    # cycle through generations
    while answer not in parrent_array:
        # choose function based on fitnes
        new_generation = []
        cube = random.randint(0, 5) # choose function
        if cube > 2:
            for a in range(len(array_of_fitnes)):
                new_generation.append(parrent_array[choose_roulette(array_of_fitnes)])
        else:
            for a in range(len(array_of_fitnes)):
                new_generation.append(parrent_array[choose_order(array_of_fitnes)])
        
        # crossover
        new_generation = crossover(new_generation)
        break

        # mutation

        # change generations
        parrent_array = new_generation

    if answer in parrent_array:
        print(parrent_array.index(answer))
        
