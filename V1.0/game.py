import random as rand

from dataclasses import dataclass
from typing import TypeVar

def PrintS (arr):
	print('----- ----- -----')
			  #!right					 #!left
	print(f"| {arr[0]} | | {arr[1]} | | {arr[2]} |") #!down
	print('----- ----- -----')
	print(f"| {arr[3]} | | {arr[4]} | | {arr[5]} |")
	print('----- ----- -----')
	print(f"| {arr[6]} | | {arr[7]} | | {arr[8]} |") #!up
	print('----- ----- -----')


def Checker(s: TypeVar("Settings", bound="Settings")):
	'''
	Control to end of a game
	'''
	if s.arr == s.answer:
		return True
	return False


class Settings():
	'''
	class to store answer array and random generated array, where:
	:answer: answer array
	:arr: random generated array
	:step: next step that user will do
	'''
	def __init__(self):
		self.answer = [1, 2, 3, 4, 5, 6, 7, 8, ' ']
		self.arr = self.answer[:]
		rand.shuffle(self.arr)
		self.step = "l"

	def __hash__(self) -> int:
		return hash("".join([f"{i}" for i in self.arr]))

	def __copy__(self) -> 'Settings':
		new = Settings()
		new.answer = self.answer[:]
		new.arr = self.arr[:]
		new.step = self.step
		return new

	def change(self):
		'''
		fun to make step, changing arr
		:return: None
		'''
		ind = self.arr.index(' ')
		if self.step == 'l':
			tmp = self.arr[ind+1]
			self.arr[ind+1] = ' '
			self.arr[ind] = tmp
		if self.step == 'r':
			tmp = self.arr[ind-1]
			self.arr[ind-1] = ' '
			self.arr[ind] = tmp
		if self.step == 'u':
			tmp = self.arr[ind+3]
			self.arr[ind+3] = ' '
			self.arr[ind] = tmp
		if self.step == 'd':
			tmp = self.arr[ind-3]
			self.arr[ind-3] = ' '
			self.arr[ind] = tmp


def AskForStep(s: TypeVar("Settings", bound="Settings")):
	'''
	function, that controls what steps can user do and asking him to make step
	:ind: index of emptiness
	:return: step
	'''
	ind = s.arr.index(' ')
	if ind == 0:
		while True:
			step = input("where should we go? (l, u): ")
			if step in ("l", "u"):
				return step
			print("\nYou missclicked and wrote smth diff from options.\n")
	if ind == 1:
		while True:
			step = input("where should we go? (l, r, u): ")
			if step in ("l", "r", "u"):
				return step
			print("\nYou missclicked and wrote smth diff from options.\n")
	if ind == 2:
		while True:
			step = input("where should we go? (r, u): ")
			if step in ("r", "u"):
				return step
			print("\nYou missclicked and wrote smth diff from options.\n")
	if ind == 3:
		while True:
			step = input("where should we go? (l, u, d): ")
			if step in ("l", "u", "d"):
				return step
			print("\nYou missclicked and wrote smth diff from options.\n")
	if ind == 5:
		while True:
			step = input("where should we go? (r, u, d): ")
			if step in ("r", "u", "d"):
				return step
			print("\nYou missclicked and wrote smth diff from options.\n")
	if ind == 6:
		while True:
			step = input("where should we go? (l, d): ")
			if step in ("l", "d"):
				return step
			print("\nYou missclicked and wrote smth diff from options.\n")
	if ind == 7:
		while True:
			step = input("where should we go? (l, r, d): ")
			if step in ("l", "r", "d"):
				return step
			print("\nYou missclicked and wrote smth diff from options.\n")
	if ind == 8:
		while True:
			step = input("where should we go? (r, d): ")
			if step in ("r","d"):
				return step
			print("\nYou missclicked and wrote smth diff from options.\n")
	while True:
		step = input("where should we go? (l, r, u, d): ")
		if step in ("l", "r", "u", "d"):
			return step
		print("\nYou missclicked and wrote smth diff from options.\n")


def GameStart():
	'''
	Main Function that starts game, works if only start game.py
	as a module
	'''
	s = Settings()
	print("\nHi dear User, its 8 puzzle game. Game looks like this: ")
	while True:
		PrintS(s.arr)
		s.step = AskForStep(s)
		s.change()
		if Checker(s):
			print("\nYou won.\n")
			break


def module():
	'''
	Function to create answer and playing deck,
	after to put into brain.py
	:return: class, of answer array and playing array
	'''
	s = Settings()
	return s


if __name__ == '__main__':
	GameStart()