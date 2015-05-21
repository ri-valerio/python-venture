#!/usr/bin/python3

def main():
	testfunc(2)
	testfunc(2, 3)
	testfunc(2, 5, 7)

	my_awesome_function(2)
	my_awesome_function()
	my_awesome_function(4)

	my_extended_args_function(1,2,3,4)
	my_kwargs_function(one = 1, two = 2, three = 3)

	my_all_args_and_kwargs_function(1, 2, 7, 8, 9, bazinga = "sheldon", scorpion = "on")


# attention the "None" keyword is awesome
def testfunc(a, b = None, c = 4):
	if b is None:
		print("How cool is that?")

	print('This is a test function', a, b, c)


def my_awesome_function(a = 7):
	for i in range(a, 10):
		print(i, end="")
	print()

def my_extended_args_function(*args):
	print(args)

def my_kwargs_function(**kwargs):
	print(kwargs['one'], kwargs['two'])

def my_all_args_and_kwargs_function(this, that, *args, **kwargs):
	print(this, that, args, kwargs["bazinga"], kwargs["scorpion"])



if __name__ == "__main__": main()
