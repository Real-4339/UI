import game as gm
import brain as br
import tracemalloc
import unittest
import time

'''
Осталось еще:
1)history
2)графы
3)ine rozmery hry
4)documentation
'''

def main_1():
	s = gm.Settings()
	s.arr = s.answer[:]
	s.arr[0] = 8
	s.arr[1] = 7
	s.arr[2] = 6
	s.arr[3] = 5
	s.arr[4] = 4
	s.arr[5] = 3
	s.arr[6] = 2
	s.arr[7] = ' '
	s.arr[8] = 1
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

def main_3():
	s = gm.Settings()
	s.arr = s.answer[:]
	s.arr[0] = 3
	s.arr[1] = 5
	s.arr[2] = 6
	s.arr[3] = 4
	s.arr[4] = 8
	s.arr[5] = ' '
	s.arr[6] = 1
	s.arr[7] = 7
	s.arr[8] = 2
	
	return s

def main_4():
	s = gm.Settings()
	return s

def main_5():
	s = gm.Settings()
	s.arr = s.answer[:]
	s.arr[0] = 6
	s.arr[1] = 1
	s.arr[2] = 8
	s.arr[3] = 2
	s.arr[4] = 7
	s.arr[5] = ' '
	s.arr[6] = 4
	s.arr[7] = 3
	s.arr[8] = 5
	
	return s

class TestAI(unittest.TestCase):

	def test_board_1(self):
		s = main_1()
		count_cykls_1 = 0
		count_cykls_2 = 0
		all_time_1 = 0
		time_1 = 0
		all_time_2 = 0
		time_2 = 0
		mem_1 = 0
		mem_2 = 0
		mem_all_1 = 0
		mem_all_2 = 0

		for cykl in range(0, 20):
			try:
				start_time = time.perf_counter()
				tracemalloc.start()
				br.algoritmus(s, 1)
				mem_1 += tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				time_1 += time.perf_counter() - start_time
			except Exception as inst:
				count_cykls_1 += 1
				self.assertEqual(str(inst), "End of a game, you found a cyklus")

		for cykl in range(0, 20):
			try:
				start_time = time.perf_counter()
				tracemalloc.start()
				br.algoritmus(s, 2)
				mem_2 += tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				time_2 += time.perf_counter() - start_time
			except Exception as inst:
				count_cykls_2 += 1
				self.assertEqual(str(inst), "End of a game, you found a cyklus")

		print(time_1, time_2)
		all_time_1 = time_1/20
		all_time_2 = time_2/20
		mem_all_1 = mem_1/20
		mem_all_2 = mem_2/20
		print("\nWas counted cykls in board_1_heuristic_1: ", count_cykls_1, \
			  ", with time: ", all_time_1,"\n","with memory: ", mem_all_1, "bytes")
		print("Was counted cykls in board_1_heuristic_2: ", count_cykls_2, \
			  ", with time: ", all_time_2,"\n","with memory: ", mem_all_2, "bytes")

	def test_board_2(self):
		s = main_2()
		count_cykls_1 = 0
		count_cykls_2 = 0
		all_time_1 = 0
		time_1 = 0
		all_time_2 = 0
		time_2 = 0
		mem_1 = 0
		mem_2 = 0
		mem_all_1 = 0
		mem_all_2 = 0

		for cykl in range(0, 20):
			try:
				start_time = time.perf_counter()
				tracemalloc.start()
				br.algoritmus(s, 1)
				mem_1 += tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				time_1 += time.perf_counter() - start_time
			except Exception as inst:
				count_cykls_1 += 1
				self.assertEqual(str(inst), "End of a game, you found a cyklus")

		for cykl in range(0, 20):
			try:
				start_time = time.perf_counter()
				tracemalloc.start()
				br.algoritmus(s, 2)
				mem_2 += tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				time_2 += time.perf_counter() - start_time
			except Exception as inst:
				count_cykls_2 += 1
				self.assertEqual(str(inst), "End of a game, you found a cyklus")

		all_time_1 = time_1/20
		all_time_2 = time_2/20
		mem_all_1 = mem_1/20
		mem_all_2 = mem_2/20
		print("\nWas counted cykls in board_2_heuristic_1: ", count_cykls_1, \
			  ", with time: ", all_time_1,"\n","with memory: ", mem_all_1, "bytes")
		print("Was counted cykls in board_2_heuristic_2: ", count_cykls_2, \
			  ", with time: ", all_time_2,"\n","with memory: ", mem_all_2, "bytes")

	def test_board_3(self):
		s = main_3()
		count_cykls_1 = 0
		count_cykls_2 = 0
		all_time_1 = 0
		time_1 = 0
		all_time_2 = 0
		time_2 = 0
		mem_1 = 0
		mem_2 = 0	
		mem_all_1 = 0
		mem_all_2 = 0

		for cykl in range(0, 20):
			try:
				start_time = time.perf_counter()
				tracemalloc.start()
				br.algoritmus(s, 1)
				mem_1 += tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				time_1 += time.perf_counter() - start_time
			except Exception as inst:
				count_cykls_1 += 1
				self.assertEqual(str(inst), "End of a game, you found a cyklus")

		for cykl in range(0, 20):
			try:
				start_time = time.perf_counter()
				tracemalloc.start()
				br.algoritmus(s, 2)
				mem_2 += tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				time_2 += time.perf_counter() - start_time
			except Exception as inst:
				count_cykls_2 += 1
				self.assertEqual(str(inst), "End of a game, you found a cyklus")

		all_time_1 = time_1/20
		all_time_2 = time_2/20
		mem_all_1 = mem_1/20
		mem_all_2 = mem_2/20
		print("\nWas counted cykls in board_3_heuristic_1: ", count_cykls_1, \
			  ", with time: ", all_time_1,"\n","with memory: ", mem_all_1, "bytes")
		print("Was counted cykls in board_3_heuristic_2: ", count_cykls_2, \
			  ", with time: ", all_time_2,"\n","with memory: ", mem_all_2, "bytes")

	def test_random_board(self):
		s = main_4()
		count_cykls_1 = 0
		count_cykls_2 = 0
		all_time_1 = 0
		time_1 = 0
		all_time_2 = 0
		time_2 = 0
		mem_1 = 0
		mem_2 = 0
		mem_all_1 = 0
		mem_all_2 = 0

		for cykl in range(0, 20):
			try:
				start_time = time.perf_counter()
				tracemalloc.start()
				br.algoritmus(s, 1)
				mem_1 += tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				time_1 += time.perf_counter() - start_time
			except Exception as inst:
				count_cykls_1 += 1
				self.assertEqual(str(inst), "End of a game, you found a cyklus")

		for cykl in range(0, 20):
			try:
				start_time = time.perf_counter()
				tracemalloc.start()
				br.algoritmus(s, 2)
				mem_2 += tracemalloc.get_traced_memory()[1]
				tracemalloc.stop()
				time_2 += time.perf_counter() - start_time
			except Exception as inst:
				count_cykls_2 += 1
				self.assertEqual(str(inst), "End of a game, you found a cyklus")

		all_time_1 = time_1/20
		all_time_2 = time_2/20
		mem_all_1 = mem_1/20
		mem_all_2 = mem_2/20
		print("\nWas counted cykls in board_4_heuristic_1: ", count_cykls_1, \
			  ", with time: ", all_time_1,"\n","with memory: ", mem_all_1, "bytes")
		print("Was counted cykls in board_4_heuristic_2: ", count_cykls_2, \
			  ", with time: ", all_time_2,"\n","with memory: ", mem_all_2, "bytes")


if __name__ == '__main__':
    unittest.main()


#				None   None			 B: 25, M: 1231
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