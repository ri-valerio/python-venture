#!/usr/bin/python3

"""
there are mutable and immutable objects in python

sometimes they seem to be changing but we can make sure
of that by using the "id" function to remove any doubts

############################################################
inside the IDLE3:

	>>> x = 42
	>>> type(x)
	<class 'int'>
	>>> id(x)
	10456352             # this id...
	>>> x = 43
	>>> id(x)
	10456384 			 # is different from this!
	>>> x = 42
	>>> id(x)
	10456352   			 # but hey, is the same as this again!
	>>>
##############################################################

So...just to make sure:


Most fundamental types in Python are immutable:

	numbers, strings, tuples

Mutable objects include:

	lists, dictionaries, other objects depending upon implementation

"""
class Egg:
	"""docstring for class Egg"""

	# constructor
	def __init__(self, kind = "fried"):
		self.kind = kind

	# getter
	# self is optional, I could have used "this" for example
	def get_kind(self):
		return "Hi, I'm " + self.kind


def main():
	fried = Egg()
	print(fried.get_kind())

	scrambled = Egg("scrambled")
	print(scrambled.get_kind())



if __name__ == '__main__': main()
