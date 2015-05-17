#!/usr/bin/python3

# simple fibonacci series
# the sum of two elements defines the next set
class Fibonacci():

	# "self" is a reference to the instanciated object
	# it is a convention, it does not have to be named self per se
	# but conventions are good in programming and life in general (I said in general!!!!)
	# so I'll stick to them

	# constructor
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def series(self):
        while(True):
            yield(self.b)
            self.a, self.b = self.b, self.a + self.b


f = Fibonacci(0, 1)

for r in f.series():
    if r > 100: break
    print(r, end=' ')
