import game as gm

def main_1():
	s = gm.Settings()
	s.arr = s.answer[:]
	s.arr[0] = 4
	s.arr[1] = 6
	s.arr[2] = 2
	s.arr[3] = 5
	s.arr[4] = 3
	s.arr[5] = 8
	s.arr[6] = 1
	s.arr[7] = 7
	s.arr[8] = ' '
	return s

def main_2():
	s = gm.Settings()
	s.arr = s.answer[:]
	s.arr[0] = 7
	s.arr[1] = ' '
	s.arr[2] = 5
	s.arr[3] = 2
	s.arr[4] = 4
	s.arr[5] = 6
	s.arr[6] = 8
	s.arr[7] = 3
	s.arr[8] = 1
	
	return s

if __name__ == '__main__':
	pass

#					   None			 B: 143, M: 991
# 7 8 6  1 2 4  - 3 5  4 6 2  using=> 7 - 5
# 5 4 3  3 5 6  4 2 6  5 3 8   		  2 4 6
# 2 - 1  7 8 -  7 8 1  1 7 -   		  8 3 1

'''
Board 1:
8 2 6 
1 7 5 
3 4 m

Board 2:
1 2 3 
4 5 6 
7 8 m 
'''