import game as gm
import tests as ts

from copy import copy, deepcopy
from typing import TypeVar
from random import choice, shuffle

SettingsT = TypeVar("SettingsT", bound="Settings")

hashes: set[hash] = set()
history: tuple[list] = tuple()
heuristik = 2

def heuristika_1(s: SettingsT):
	'''
	First heuristik function
	:count: Počet políčok, ktoré nie sú na svojom mieste
	:s: class, of answer array and playing array
	:arr: random generated array
	PrintS() - function to print deck
	'''
	count = 0
	
	for index, x in enumerate(s.arr):
		if s.answer[index] != s.arr[index]:
			count += 1

	return count
	#print("\nNum of tabes that not on their places: ", count)
	
def heuristika_2(s: SettingsT):
	'''
	Second heuristik function
	PrintS() - function to print deck
	:suma: Súčet vzdialeností jednotlivých políčok od ich cieľovej pozície
	:count: ??
	:ind_not: ??
	:ind_r: ??
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
	a = list(argv)
	d = list()

	for o in a:
		print(o.arr, "tu")

	for index, agr in enumerate(a):
		if hash("".join([f"{i}" for i in agr.arr])) in hashes:
			d.append(index)

	for l in d[::-1]:
		a.pop(l)

	if a == []:
		raise ValueError("End of a game, you found a cyklus")

	return a

def do_most_relevant_step(s: SettingsT):
	'''
	Делает ходы и считает их хеуристики + hash 
	:return: will_step
	'''
	ind = s.arr.index(' ')

	print(ind, " :index")

	if ind == 0:
		array_l = deepcopy(s)
		array_l.step = "l"
		array_l.change()

		array_u = deepcopy(s)
		array_u.step = "u"
		array_u.change()

		#check hash - проверка оба хеша и убрать один если существует,
		#если все хеши - тогда все, конец, приплыли
		answ = find_min(*check_hash(array_l, array_u))

		return answ.step
		
	if ind == 1:
		array_l = deepcopy(s)
		array_l.step = "l"
		array_l.change()

		array_r = deepcopy(s)
		array_r.step = "r"
		array_r.change()

		array_u = deepcopy(s)
		array_u.step = "u"
		array_u.change()

		answ = find_min(*check_hash(array_l, array_r, array_u))

		return answ.step

	if ind == 2:
		array_r = deepcopy(s)
		array_r.step = "r"
		array_r.change()

		array_u = deepcopy(s)
		array_u.step = "u"
		array_u.change()

		answ = find_min(*check_hash(array_r, array_u))

		return answ.step

	if ind == 3:
		array_l = deepcopy(s)
		array_l.step = "l"
		array_l.change()

		array_u = deepcopy(s)
		array_u.step = "u"
		array_u.change()

		array_d = deepcopy(s)
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_l, array_u, array_d))

		return answ.step

	if ind == 5:
		array_r = deepcopy(s)
		array_r.step = "r"
		array_r.change()

		array_u = deepcopy(s)
		array_u.step = "u"
		array_u.change()

		array_d = deepcopy(s)
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_r, array_u, array_d))

		return answ.step

	if ind == 6:
		array_l = deepcopy(s)
		array_l.step = "l"
		array_l.change()

		array_d = deepcopy(s)
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_l, array_d))

		return answ.step

	if ind == 7:
		array_l = deepcopy(s)
		array_l.step = "l"
		array_l.change()

		array_r = deepcopy(s)
		array_r.step = "r"
		array_r.change()

		array_d = deepcopy(s)
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_l, array_r, array_d))

		return answ.step

	if ind == 8:
		array_r = deepcopy(s)
		print("8: ", array_r.arr)
		array_r.step = "r"
		array_r.change()

		array_d = deepcopy(s)
		print("8: ", array_d.arr)
		array_d.step = "d"
		array_d.change()

		answ = find_min(*check_hash(array_r, array_d))

		return answ.step

	array_l = deepcopy(s)
	array_l.step = "l"
	array_l.change()

	array_r = deepcopy(s)
	array_r.step = "r"
	array_r.change()

	array_d = deepcopy(s)
	array_d.step = "d"
	print("8: ", array_d.arr)
	array_d.change()

	array_u = deepcopy(s)
	array_u.step = "u"
	array_u.change()

	answ = find_min(*check_hash(array_l, array_r, array_d, array_u))

	return answ.step

def algoritmus(value = 2):
	'''
	:count_steps: count of all done steps
	'''
	global history
	global heuristik

	s = gm.module()
	#s = ts.main_2()
	count_steps = 0
	heuristik = value

	for a in range(4):
		gm.PrintS(s.arr)

		history = (*history, s.arr)

		hashes.add(hash("".join([f"{i}" for i in s.arr])))

		s.step = do_most_relevant_step(s)
		s.change()
		count_steps += 1

		if gm.Checker(s):
			print(f"\nYou won. You did {count_steps} steps\n")
			break

if __name__ == '__main__':
	algoritmus(2)