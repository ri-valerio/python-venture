#!/usr/bin/python3

# Global vs. local variables in functions

# Declare a global variable and initialize it
f = 0

def main():

	global f  # reference the global variable

	print(f)

	# re-declaring the variable works
	f = "abc"
	print(f)

	# ERROR: variables of different types cannot be combined
	#print("string type " + 123)
	print("string type " + str(123))
	# or simply
	print("string type", 123)

	someFunction()
	print(f)
	del(f)   # delete variable from memory
	print(f) # it will throw an error because the variable doesn't exist anymore

def someFunction():
	global f   # access the outside global variable
	f = "def"  # change the global variable
	print(f)


if __name__ == '__main__': main()
