#!/usr/bin/python3

def main():
	# looping lines from a file
	fh = open('lines.txt')
	for line in fh.readlines():
	    print(line, end="")

	print() # separator

	print("looping a range", end=": ")
	for x in range(1,10):
		print(x, end=" ")

	print() # separator

	print("looping a tuple", end=": ")
	for x in (1,10):
		print(x, end=" ")

	print() # separator

	print("looping a set", end=": ")
	for x in {1, 2, 3}:
		print(x, end=" ")

	print() # separator

	print("looping a list", end=": ")
	for x in [1, 2, 3]:
		print(x, end=" ")

	print() # separator

	print("looping a sequence of numbers", end=": ")
	for x in 1, 2, 3:
		print(x, end=" ")

	print() # separator

	print("looping a sequence of characters", end=": ")
	for x in 'N', 'S', 'A':
		print(x, end=" ")

	print() # separator

	print("looping each character in a string", end=": ")
	for x in "bazinga":
		print(x, end=" ")


if __name__ == "__main__": main()
