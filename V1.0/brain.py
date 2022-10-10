import game as gm
import tests as ts

from copy import copy
from typing import TypeVar
from random import choice, shuffle

SettingsT = TypeVar("SettingsT", bound="Settings")

hashes: set[hash] = set()
history: tuple[list] = tuple()
heuristik = 2 # choose one of two heuristic functions

def heuristika_1(s: SettingsT):
	'''
	First heuristik function
	:count: Počet políčok, ktoré nie sú na svojom mieste
	:s: class, of answer array and playing array
	:arr: random generated array
	:return: int() 
	'''
	count = 0
	
	for index, x in enumerate(s.arr):
		if s.answer[index] != s.arr[index]:
			count += 1

	return count
	
def heuristika_2(s: SettingsT):
	'''
	Second heuristik function

	:suma: Súčet vzdialeností jednotlivých políčok od ich cieľovej pozície
	:count: counts small steps from current "uzol" to "cielovy uzol"
	:ind_not: index of deck which NOT on his place
	:ind_r: index of deck which on his place
	:return: int()
	'''
	suma = 0

	for c in range(0, 9):
		count = 0
		if s.answer[c] == s.arr[c]:
			continue
		ind_not = s.arr.index(s.answer[c])
		ind_r = s.answer.index(s.answer[c])

		if ind_not in (0, 1, 2):
			if ind_r in (0, 1, 2):
				count = abs(ind_r - ind_not)
				suma += count
				continue
			if ind_r in (3, 4, 5):
				count += 1
				ind_not += 3
				count += abs(ind_r - ind_not)
				suma += count
				continue
			if ind_r in (6, 7, 8):
				count += 2
				ind_not += 6
				count += abs(ind_r - ind_not)
				suma += count
				continue

		if ind_not in (3, 4, 5):
			if ind_r in (0, 1, 2):
				count += 1
				ind_not -= 3
				count += abs(ind_r - ind_not)
				suma += count
				continue
			if ind_r in (3, 4, 5):
				count = abs(ind_r - ind_not)
				suma += count
				continue
			if ind_r in (6, 7, 8):
				count += 1
				ind_not += 3
				count += abs(ind_r - ind_not)
				suma += count
				continue

		if ind_not in (6, 7, 8):
			if ind_r in (0, 1, 2):
				count += 2
				ind_not -= 6
				count += abs(ind_r - ind_not)
				suma += count
				continue
			if ind_r in (3, 4, 5):
				count += 1
				ind_not -= 3
				count += abs(ind_r - ind_not)
				suma += count
				continue
			if ind_r in (6, 7, 8):
				count = abs(ind_r - ind_not)
				suma += count
				continue
	return suma

def find_min(*argv):
	'''
	Function to find min price based on heuristic function
	
	:*argv: set of classes
	:return: class(Settings)
	'''

	rad: dict[SettingsT, int] = {}

	if heuristik == 2:
		for agr in argv:
			rad[agr] = heuristika_2(agr)
	else:
		for agr in argv:
			rad[agr] = heuristika_1(agr)

	mval = min(rad.values())
	rad = [k for k, v in rad.items() if v == mval]

	return choice(rad)

def check_hash(*argv):
	global history
	global hashes
	'''
	Check hashes and get rid off states(boards) i was in if there are some,
	If returns None - than its end of a game, there are no more steps i can make
	
	:argv: set of classes
	:return: list of classes i can work with
	'''
	a = list(argv)
	d = list()

	for index, agr in enumerate(a):
		if hash("".join([f"{i}" for i in agr.arr])) in hashes:
			d.append(index) # puts indexes of classes i need to delete from a

	for l in d[::-1]:
		a.pop(l)

	if a == []:
		history = ()
		hashes = set()
		raise ValueError("End of a game, you found a cyklus")

	return a

def do_most_relevant_step(s: SettingsT):
	'''
	Makes new boards with steps based on main board which is (s),
	also checks hashes.

	:return: str(will_step)
	'''
	ind = s.arr.index(' ')

	if ind == 0:
		array_l = s.__copy__()
		array_l.step = "l"
		array_l.change()

		array_u = s.__copy__()
		array_u.step = "u"
		array_u.change()

		answ = find_min(*check_hash(array_l, array_u))

		return answ.step
		
	if ind == 1:
		array_l = s.__copy__()
		array_l.step = "l"
		array_l.change()

		array_r = s.__copy__()
		array_r.step = "r"
		array_r.change()

		array_u = s.__copy__()
		array_u.step = "u"
		array_u.change()

		answ = find_min(*check_hash(array_l, array_r, array_u))

		return answ.step

	if ind == 2:
		array_r = s.__copy__()
		array_r.step = "r"
		array_r.change()

		array_u = s.__copy__()
		array_u.step = "u"
		array_u.change()

		answ = find_min(*check_hash(array_r, array_u))
		
		return answ.step

	if ind == 3:
		array_l = s.__copy__()
		array_l.step = "l"
		array_l.change()

		array_u = s.__copy__()
		array_u.step = "u"
		array_u.change()

		array_d = s.__copy__()
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_l, array_u, array_d))
		
		return answ.step

	if ind == 5:
		array_r = s.__copy__()
		array_r.step = "r"
		array_r.change()

		array_u = s.__copy__()
		array_u.step = "u"
		array_u.change()

		array_d = s.__copy__()
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_r, array_u, array_d))
		
		return answ.step

	if ind == 6:
		array_l = s.__copy__()
		array_l.step = "l"
		array_l.change()

		array_d = s.__copy__()
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_l, array_d))
		
		return answ.step

	if ind == 7:
		array_l = s.__copy__()
		array_l.step = "l"
		array_l.change()

		array_r = s.__copy__()
		array_r.step = "r"
		array_r.change()

		array_d = s.__copy__()
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_l, array_r, array_d))
		
		return answ.step

	if ind == 8:
		array_r = s.__copy__()
		#print("8: ", array_r.arr)
		array_r.step = "r"
		array_r.change()

		array_d = s.__copy__()
		#print("8: ", array_d.arr)
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_r, array_d))
		
		return answ.step

	array_l = s.__copy__()
	array_l.step = "l"
	array_l.change()

	array_r = s.__copy__()
	array_r.step = "r"
	array_r.change()

	array_d = s.__copy__()
	array_d.step = "d"
	#print("8: ", array_d.arr)
	array_d.change()

	array_u = s.__copy__()
	array_u.step = "u"
	array_u.change()

	answ = find_min(*check_hash(array_l, array_r, array_d, array_u))

	if answ == None:
		return answ
		
	return answ.step

def algoritmus(s: SettingsT, value = 2):
	'''
	PrintS() - function to print deck

	:s: class(starting board)
	:value: value of heuristic fun
	:count_steps: count of all done steps
	'''
	global history
	global hashes
	global heuristik

	count_steps = 0
	heuristik = value

	while True:
		#gm.PrintS(s.arr)

		history = (*history, s.arr)
		print("arr ", s.arr)
		#history = history + (s.arr,)
		#history.append(s.arr)
		print(history)

		hashes.add(hash("".join([f"{i}" for i in s.arr])))

		s.step = do_most_relevant_step(s)

		s.change()
		count_steps += 1

		if gm.Checker(s):
			#print(f"\nYou won. You did {count_steps} steps\n")
			#his = tuple(history)
			#print(his)
			history = ()
			hashes = set()
			return True #[count_steps, his]

if __name__ == '__main__':
	#s = gm.module()
	s = ts.main_1()
	algoritmus(s, 2)
	# l = 0
	# his = ()
	# for r in range(0, 50):
	# 	try:
	# 		arr = algoritmus(s, 2)
	# 		l = arr[0]
	# 		his = arr[1] 
	# 	except Exception as e:
	# 		pass
	# 	else:
	# 		print(his)
	# 		# if l == 2 or l == 4:
	# 		# 	print(his)
	# 	finally:
	# 		print(l)