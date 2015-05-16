#!/usr/bin/python3

class Person():
	def __init__(self, name, age, favorite_color):
		self.name           = name
		self.age            = age
		self.favorite_color = favorite_color

	def print_person_info(self):
		print(" Name:"           , self.name, "\n",
		       "Age:"            , self.age, "\n",
		       "Favorite Color:" , self.favorite_color)


def main():

	# YAAAAYYYY: named params in instances of classes - aka - objects =)
	ricardo = Person(name = "Ricardo Valério", age  = 24, favorite_color = "Purpure")
	ricardo.print_person_info()

	print()

	silvia = Person(name = "Sílvia Valério", age  = 31, favorite_color = "Aqua Blue")
	silvia.print_person_info()




if __name__ == '__main__':
	main()
