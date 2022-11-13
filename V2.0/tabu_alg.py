import random
import classes

def tabu_algorithm():
    """
    Tabu search algorithm
    1 - Generate a random solution based on Greedy algorithm, which is the best solution and current solution
    2 - Generate a list of neighbors for the solution (10) using mutations based on current solution
    3 - Find the best neighbor it will be current solution, compare it with the best solution
    4 - Add the best solution to the tabu set if best is changed
    5 - If the best solution is not changed, then go to step 2 and repeat the process
    """
    # 1 - Generate a random solution based on Greedy algorithm, which is the best solution and current solution
    cities = map = classes.generator()
    best_solution = cities.greedy_answer()
    current_solution = best_solution.copy()
    tabu_tenure = 100

    # print first best solution
    print("First best solution: ", [city.index for city in best_solution], calculate_total_distance(best_solution))

    # 2 - Generate a list of neighbors for the solution (10) using mutations based on current solution
    tabu_set:set = set()
    tabu_set.add(calculate_total_distance(best_solution))
    for a in range(100000):
        neighbors = generate_neighbors(current_solution)
        # 3 - Find the best neighbor it will be current solution, compare it with the best solution
        current_solution = fitness(neighbors)
        # 4 - Add the best solution to the tabu set if best is changed
        if calculate_total_distance(current_solution) < calculate_total_distance(best_solution):
            best_solution = current_solution.copy()
            tabu_set.add(calculate_total_distance(best_solution))
            if len(tabu_set) > tabu_tenure:
                tabu_set.pop()
        # 5 - If the best solution is not changed, then go to step 2 and repeat the process
    
    print("Best solution is:", [city.index for city in best_solution])
    print(f"Total distance is: {calculate_total_distance(best_solution)} km")

def generate_neighbors(solution:list[classes.City]) -> list[list[classes.City]]:
    neighbors = []
    cube = [mutation_1, mutation_2]
    
    for a in range(10):
        neighbor = solution.copy()
        neighbors.append(cube[random.randint(0,1)](neighbor))
    return neighbors

def mutation_1(array: list[classes.City]) -> list[classes.City]:
    # mutation function
    # 1 - Swap two cities
    index_1 = random.randint(0, len(array)-1)
    if index_1 == len(array)-1:
        index_2 = len(array)-2
    elif index_1 == 0:
        index_2 = 1
    else:
        index_2 = random.choice([index_1-1, index_1+1])
    #print("mutation", index_1, index_2, ind)
    array[index_1], array[index_2] = array[index_2], array[index_1]
    return array

def mutation_2(array: list[classes.City]) -> list[classes.City]:
    # mutation function
    # 2 - Pick two cities and reverse the order of the cities between them
    index_1 = random.randint(0, len(array)-1)
    while True:
        index_2 = random.randint(0, len(array)-1)
        if index_2 != index_1:
            break
    if index_1 > index_2:
        index_1, index_2 = index_2, index_1
        
    array[index_1:index_2+1] = array[index_1:index_2+1][::-1]
    return array

def fitness(solution: list[list[classes.City]]) -> list[classes.City]:
    # fitness function
    # 3 - Find the best neighbor it will be current solution
    current_solution = solution[0]
    for neighbor in solution:
        if calculate_total_distance(neighbor) < calculate_total_distance(current_solution):
            current_solution = neighbor
    return current_solution

def calculate_total_distance(solution: list[classes.City]) -> float:
    # calculate total distance
    total_distance = 0
    for a in range(len(solution)-1):
        total_distance += classes.distance(solution[a].x, solution[a].y, solution[a+1].x, solution[a+1].y)
    return total_distance