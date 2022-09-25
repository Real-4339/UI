import game as gm

def main_1():
	s = gm.Settings()
	s.arr = s.answer[:]
	s.arr[2] = 4
	s.arr[3] = 3
	return s

if __name__ == '__main__':
	pass
	
# 7 8 6  1 2 4
# 5 4 3  3 5 6
# 2 - 1  7 8 -