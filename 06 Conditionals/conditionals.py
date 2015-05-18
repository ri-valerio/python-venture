#!/usr/bin/python3

def main():
	a, b = 0, 1

	if a < b:
		print("a is less than b")
	elif a == b:
		print("a is equal to b")
	else:
		print("a is greater than b")


	is_it_true = "this is true" if a < b else "this is not true"

	# the line above do the same of all these next lines above
	# if a < b:
	# 	is_it_true = "this is true"
	# else:
	# 	is_it_true = "this is not true"

	print(is_it_true)


if __name__ == "__main__": main()
