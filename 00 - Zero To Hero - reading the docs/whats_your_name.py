#!/usr/bin/python3


def main():

	name = whats_your_name()
	print("Hello, " + name)
	print(name + " let's calculate the area of a triangle")

	width  = int(input("Enter the width: "))
	height = int(input("Now enter the height: "))
	area   = area_of_a_triangle(width, height)

	print("BTW, just to say first that I have %d cats" % 3)

	print("The area of the triangle is %.1f cms squared" % area)


# function that asks a person's name and returns it to print it
def whats_your_name():
	name = input("Enter your name: ")
	return name

# function that calculate the area of a triangle
def area_of_a_triangle(width, height):
	return width * height / 2



if __name__ == '__main__':
	main()
