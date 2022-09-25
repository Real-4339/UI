import game as gm
import tests as ts

def heuristika():
	"""
	count - Počet políčok, ktoré nie sú na svojom mieste
	suma - Súčet vzdialeností jednotlivých políčok od ich cieľovej pozície
	 ? - Kombinácia predchádzajúcich odhadov
	"""
	#s = gm.module()
	s = ts.main_1()
	count = 0
	suma = 0
	
	for index, x in enumerate(s.arr):
		if s.answer[index] != s.arr[index]:
			count += 1
	print("\nNum of tabes that not on their places: ", count)
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
				ind_not += 3
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
	print("Súčet vzdialeností jednotlivých políčok od ich cieľovej pozície: ", suma)		
	gm.PrintS(s.arr)

def uzol():
	pass

def algoritmus():
	pass

if __name__ == '__main__':
	heuristika()