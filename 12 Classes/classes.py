#!/usr/bin/python3

class Duck:
	def __init__(self, name):
		self.name = name

	def quack(self):
	    print('Quaaack!')

	def walk(self):
	    print('Walks like a duck.')

def main():
    donald = Duck(name = "Donald")
    print(donald.name)
    donald.quack()
    donald.walk()

if __name__ == "__main__": main()
