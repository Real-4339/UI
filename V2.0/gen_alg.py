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

    # print("origin array")
    # for r in array:
    #     print([c.index for c in r])
    
    # put not changed vectors into new generation
    for a in range(len(array)):
        if a not in indexes_of_permutations:
            #print(a, 'not in')
            new_generation[a] = array[a] # type: ignore
            #new_generation.append(array[a])
    
    # print("new gen before")
    # for r in new_generation:
    #     if not isinstance(r, int):
    #         print([c.index for c in r]) # type: ignore

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
                    #print(b[i]) 

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

def choose_roulette(array_of_fitnes: list) -> int: # bad desigeon, cause we need to find min not max
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

def choose_tournament(array_of_fitnes: list) -> int:
    # choose function (tournament)
    min_array = []
    min_array.append(array_of_fitnes.index(min(array_of_fitnes)))
    new_min = max(array_of_fitnes)
    new_index = -1
    #print(array_of_fitnes)
    #print(array_of_fitnes.index(min(array_of_fitnes)))
    #print(min_array, "printing min array")
    for i in range(len(array_of_fitnes)//2):
        for ind, a in enumerate(array_of_fitnes):
            if ind not in min_array and a < new_min:
                new_min = a
                new_index = ind
                #print(new_index, "printing new index")
                #print(min_array, "printing min array in cycle")
        if new_index != -1:
            min_array.append(new_index)
            new_min = max(array_of_fitnes)
            new_index = -1
    
    print('min arr')
    print([c for c in min_array])

    return min_array[random.randint(0, len(min_array)-1)]

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

def mutation(array: list[list[classes.City]]) -> list[list[classes.City]]:
    # mutation function
    mutation_rate: float = 0.1
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

def best(array: list[list[classes.City]], array_of_fitness: list[float]) -> tuple[int]:
    # best function
    best = min(array_of_fitness)
    best_index = array_of_fitness.index(best)
    
    arr_2 = array_of_fitness.copy()
    arr_2.remove(best)
    best_2 = min(arr_2)
    best_2_index = array_of_fitness.index(best_2)
    
    arr_3 = arr_2.copy()
    arr_3.remove(best_2)
    best_3 = min(arr_3)
    best_3_index = array_of_fitness.index(best_3)

    return best_index, best_2_index, best_3_index
    

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
    for a in range(1000):
        # choose function based on fitnes
        new_generation = []

        # # append best 3 vectors to new generation
        b1, b2, b3 = best(parrent_array, array_of_fitnes)
        new_generation.append(parrent_array[b1])
        new_generation.append(parrent_array[b2])
        new_generation.append(parrent_array[b3])

        if fitnes(parrent_array[b1]) < best_num:
            best_num = fitnes(parrent_array[b1])
            best_array = parrent_array[b1]


        # print("parent array in cycle")
        # for r in parrent_array:
        #     print([c.index for c in r])
        

        cube = random.randint(0, 5) # choose function
        if cube > 2:
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

        # print("new generation in cycle")
        # for r in new_generation:
        #     print([c.index for c in r])

        # mutation
        new_generation = mutation(new_generation)

        # print("new generation in cycle after mutation")
        # for r in new_generation:
        #     print([c.index for c in r])

        # change generations
        parrent_array = new_generation
        
        # add fitnes to array_of_fitnes
        for u in range(20):
            #print([c.index for c in parrent_array[u]])
            array_of_fitnes.append(fitnes(parrent_array[u]))

        counter += 1
        #print(min(array_of_fitnes), counter, "answer fitnes", fintes_answer)

    
    # check answer
    print("Greedy answer: ", answer_index, "fitnes: ", fintes_answer)
    print("Best now: ", [c.index for c in parrent_array[best(parrent_array, array_of_fitnes)[0]]], "fitnes: ", min(array_of_fitnes))
    print("Best ever: ", [c.index for c in best_array], "fitnes: ", best_num)
   
    
    
    