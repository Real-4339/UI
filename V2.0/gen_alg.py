import random
import classes


def fitnes(array: list[classes.City]) -> float:
    return sum(classes.distance(array[a].x, array[a].y, array[a+1].x, array[a+1].y) for a in range(len(array)-1))

def new_permutation(array: list[list[classes.City]]) -> tuple[list[list[classes.City]], list[int]]:
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
    
    # for a in array:
    #     print([c.index for c in a])
    # print("permutations", len(permutations))
    # for a in permutations:
    #     print([c.index for c in a])

    return permutations, restrictions

def crossover(array: list[list[classes.City]]) -> list[list[classes.City]]:
    # choose two vectors
    permutation, indexes_of_permutations = new_permutation(array) # list of cities that need to be csossed
    # choose n-1 cities in first vector
    # add other using order from second vector
    index_a_1 = 0
    index_a_2 = 0

    index_b_1 = 0
    index_b_2 = 0
    new_generation = [0] * len(array)

    arr_a = []
    arr_b = []
    ind = -2

    # put not changed vectors into new generation
    for a in range(len(array)):
        if a not in indexes_of_permutations:
            new_generation[a] = array[a] # type: ignore
    

    # put changed vectors into new generation
    for a, b in [permutation[i:i+2] for i in range(0, len(permutation), 2)]:
        arr_a = []
        arr_b = []
        diff_1 = 0
        diff_2 = 0
        ind += 2

        # print('-----------------------')
        # print("a", [c.index for c in a])
        # print("b", [c.index for c in b])
        
        while diff_1 == 0 or diff_1 == len(a)-1:
            index_a_1 = random.randint(0, len(a)-1)
            index_a_2 = random.randint(0, len(a)-1)
            diff_1 = abs(index_a_1 - index_a_2)

        while diff_2 == 0 or diff_2 == len(b)-1:
            index_b_1 = random.randint(0, len(b)-1)
            index_b_2 = random.randint(0, len(b)-1)
            diff_2 = abs(index_b_1 - index_b_2)

        a_c = []
        b_c = []
        bc = 0
        ac = 0

        #print('diff1', diff_1, 'diff2', diff_2, index_a_1, index_a_2, index_b_1, index_b_2)

        if index_a_1 > index_a_2:
            #print ("a1 > a2")
            
            for i in range (len(b)): # that need to be added to a + array of indexes
                if b[i] not in a[index_a_2:index_a_1 + 1]:
                    b_c.append(b[i])

            #print([c.index for c in a[index_a_2:index_a_1+1]])

            u = 0
            while u < len(b):
                if u == index_a_2:
                    for c in range (index_a_2, index_a_1 + 1):
                        arr_a.append(a[c])
                    u += diff_1
                else:
                    arr_a.append(b_c[bc])
                    bc += 1
                u += 1
            
            new_generation[indexes_of_permutations[ind]] = arr_a 
        else:
            #print ("a1 < a2")
            for i in range (len(b)): # that need to be added to a + array of indexes
                if b[i] not in a[index_a_1:index_a_2 + 1]:
                    b_c.append(b[i]) 
                    #print(b[i])
            
            #print([c.index for c in a[index_a_1:index_a_2+1]])

            u = 0
            while u < len(b):
                if u == index_a_1:
                    for c in range (index_a_1, index_a_2 + 1):
                        arr_a.append(a[c])
                    u += diff_1
                else:
                    arr_a.append(b_c[bc])
                    bc += 1
                u += 1

            new_generation[indexes_of_permutations[ind]] = arr_a 

        if index_b_1 > index_b_2:
            #print ("b1 > b2")
            for i in range (len(a)): # that need to be added to b + array of indexes
                if a[i] not in b[index_b_2:index_b_1 + 1]:
                    a_c.append(a[i])
                    #print(a[i])

            #print([c.index for c in b[index_b_2:index_b_1 + 1]])

            u = 0
            while u < len(a):
                if u == index_b_2:
                    for c in range (index_b_2, index_b_1 + 1):
                        arr_b.append(b[c])
                    u += diff_2
                else:
                    arr_b.append(a_c[ac])
                    ac += 1
                u += 1

            new_generation[indexes_of_permutations[ind+1]] = arr_b
        else:
            #print ("b1 < b2")
            for i in range (len(a)): # that need to be added to b + array of indexes
                if a[i] not in b[index_b_1:index_b_2 + 1]:
                    a_c.append(a[i])
                    #print(a[i])
            
            #print([c.index for c in b[index_b_1:index_b_2 + 1]])

            u = 0
            while u < len(a):
                if u == index_b_1:
                    for c in range (index_b_1, index_b_2 + 1):
                        arr_b.append(b[c])
                    u += diff_2
                else:
                    arr_b.append(a_c[ac])
                    ac += 1
                u += 1

            new_generation[indexes_of_permutations[ind+1]] = arr_b
        
        # print("array")
        # for r in array:
        #     print([c.index for c in r])
        # print("permutations")
        # for r in permutation:
        #     print([c.index for c in r])
        # print("indexes: ", indexes_of_permutations)
        # for r in new_generation:
        #     if not isinstance(r, int):
        #         print([c.index for c in r]) # type: ignore
        
        # if ind == 10:
        #     break

    # print("array")
    # for r in array:
    #     print([c.index for c in r])
    # print("permutations")
    # for r in permutation:
    #     print([c.index for c in r])
    # print("indexes: ", indexes_of_permutations)
    # for r in new_generation:
    #     print([c.index for c in r])

    return new_generation

def choose_roulette(array_of_fitnes: list) -> int:
    # choose function (roulette)
    arr_copy = [1/n for n in array_of_fitnes]
    
    index = random.choices(range(len(array_of_fitnes)), weights=arr_copy)
    return index[0]
    
    # S = int(sum(cc for cc in array_of_fitnes))
    
    # r = random.randint(0, S-1)
    # max = 0
    # index = -1

    # for ind, a in enumerate(array_of_fitnes):
    #     max += a
    #     if max > r:
    #         index = ind
    #         break
    
    # return index
   

def choose_tournament(array_of_fitnes: list) -> int: # scatyvaetsa v local minima
    # choose function (tournament)
    min_array = []
    min_array.append(array_of_fitnes.index(min(array_of_fitnes)))
    new_min = max(array_of_fitnes)
    new_index = -1
    for i in range(len(array_of_fitnes)//2):
        for ind, a in enumerate(array_of_fitnes):
            if ind not in min_array and a < new_min:
                new_min = a
                new_index = ind
        if new_index != -1:
            min_array.append(new_index)
            new_min = max(array_of_fitnes)
            new_index = -1
    
    print('min arr')
    print([c for c in min_array])

    return min_array[random.randint(0, len(min_array)-1)]

def choose_order(array_of_fitnes: list) -> int:
    # array_of_fitnes.sort()
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

def mutation(array: list[list[classes.City]]) -> list[list[classes.City]]:
    # mutation function
    mutation_rate: float = 0.7
    for ind, a in enumerate(array):
        if random.random() < mutation_rate:
            index_1 = random.randint(0, len(a)-1)
            if index_1 == len(a)-1:
                index_2 = len(a)-2
            elif index_1 == 0:
                index_2 = 1
            else:
                index_2 = random.choice([index_1-1, index_1+1])
            #print("mutation", index_1, index_2, ind)
            a[index_1], a[index_2] = a[index_2], a[index_1]
            array[ind] = a
    return array

def mutation_2(array: list[classes.City]) -> list[classes.City]:
    # mutation function
    # 2 - Pick two cities and reverse the order of the cities between them
    mutation_rate: float = 0.3
    if random.random() > mutation_rate:
        return array
    
    index_1 = random.randint(0, len(array)-1)
    while True:
        index_2 = random.randint(0, len(array)-1)
        if index_2 != index_1:
            break
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1
        
    array[index_1:index_2+1] = array[index_1:index_2+1][::-1]
    return array

def mutation_3(array: list[classes.City]) -> list[classes.City]:
    # mutation function
    # 3 - Pick two random cities and reverse them

    mutation_rate: float = 0.1
    if random.random() > mutation_rate:
        return array
    index_1 = random.randint(0, len(array)-1)
    while True:
        index_2 = random.randint(0, len(array)-1)
        if index_2 != index_1:
            break

    array[index_1], array[index_2] = array[index_2], array[index_1]
    
    return array


def best(array: list[list[classes.City]], array_of_fitness: list[float]) -> tuple[int]:
    # best function
    arr_copy: list[tuple[int, float]] = [a for a in enumerate(array_of_fitness)]
    arr_copy.sort(key=lambda x: x[1])

    return arr_copy[0][0], arr_copy[1][0], arr_copy[2][0]

def genetics_algorithm():
    map = classes.generator()
    answer = map.greedy_answer() # answer vektor of cities: list
    answer_index = [c.index for c in answer] 
    parrent_array = [] # list of vectors
    array_of_fitnes = [] # list of fitnes
    counter = 0 # counter of generations
    fintes_answer = fitnes(answer) # fitnes of answer
    best_num = 10000
    best_array = []

    # first generation
    u = 0
    while u < 20:
        arr = answer[:]
        random.shuffle(arr)
        if arr not in parrent_array:
            array_of_fitnes.append(fitnes(arr))
            parrent_array.append(arr)
        else:
            u -= 1
        u += 1
    
    # cycle through generations
    for a in range(50000):
        # choose function based on fitnes
        new_generation = []

        # append best 3 vectors to new generation
        b1, b2, b3 = best(parrent_array, array_of_fitnes)
        new_generation.append(parrent_array[b1])
        new_generation.append(parrent_array[b2])
        new_generation.append(parrent_array[b3])

        if fitnes(parrent_array[b1]) < best_num:
            best_num = fitnes(parrent_array[b1])
            best_array = parrent_array[b1]

        # for a in range(len(array_of_fitnes)-3):
        #     new_generation.append(parrent_array[choose_roulette(array_of_fitnes)])

        cube = random.randint(0, 5) # choose function
        if cube > 0:
            for a in range(len(array_of_fitnes)-3):
                new_generation.append(parrent_array[choose_roulette(array_of_fitnes)])
        else:
            for a in range(len(array_of_fitnes)-3):
                new_generation.append(parrent_array[choose_order(array_of_fitnes)])
        
        # clean array_of_fitnes
        array_of_fitnes = []

        if new_generation == []:
            print("new_generation is empty, v2")

        # crossover
        new_generation = crossover(new_generation)

        # mutation
        if cube > 3:
            new_generation = mutation(new_generation)
        if cube > 1:
            new_generation = [mutation_2(a) for a in new_generation]
        else:
            new_generation = [mutation_3(a) for a in new_generation]

        # change generations
        parrent_array = new_generation
        
        # add fitnes to array_of_fitnes
        for u in range(20):
            array_of_fitnes.append(fitnes(parrent_array[u]))

        counter += 1
        #print(min(array_of_fitnes), counter, "answer fitnes", fintes_answer)

    
    # check answer
    print("Fitnesess:", array_of_fitnes)
    print("Greedy:", answer_index, fintes_answer)
    print("Best now: ", [c.index for c in parrent_array[best(parrent_array, array_of_fitnes)[0]]], "fitnes: ", min(array_of_fitnes))
    print("Best ever: ", [c.index for c in best_array], "fitnes: ", best_num)
   
    
    
    