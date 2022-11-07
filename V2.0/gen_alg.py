import classes


def fitnes(array: list) -> int:
    ...

def genetics_algorithm():
    # first generation
    old_map = classes.generator()
    answer = old_map.answer() # find answer
    # choice of the best
    # crossover
    # mutation
    # cycle through generations
    # while new_map.answer() != answer:
    #     new_map = classes.generator()
    #     if new_map.answer() < answer:
    #         answer = new_map.answer()
    #         old_map = new_map
    