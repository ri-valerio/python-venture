#
# Example file for working with functions
#

# define a function
def func1():
  print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
  print(arg1, arg2)

# function that returns a value
def cube(x):
  return x*x*x

# function with default value for an argument
def power(num, x=1):
  return num ** x

#function with variable number of arguments
def multi_add(*args):
  result = 0;
  for x in args:
    result = result + x
  return result


def area_of_triangle(width = 0, height = 0):
  return width * height / 2


func1()             # simple function call

print(func1())      # will print something and then prints "None"
                    # because the function doesn't return anything

print(func1)        # print the address location of the function object

func2(10,20)        # simple function call with two paramaters

print(func2(10,20)) # will print something and then prints "None" again
                    # because the function doesn't return anything

print(cube(3))    # simple function call
print(power(2))   # simple function call
print(power(2,3)) # simple function call

print(power(x = 3, num = 2)) # reversing the order of the paramaters in
                             # respect to the order of the arguments definition,
                             # but yet, because we define the name of them,
                             # they will be correctly associated
                             # within the function itself


# OMG, this is really useful! think about it:
# When you have bazillions of arguments to be passed and then later
# you try to read what you have coded let's say, one week ago
# and you look like a donkey looking to your own code thinking:
# "what a hell in the universe this shit is about???!!"
# definitely, from now on, I'll try to code all my functions
# with named params, FTW bitch!
# What do you think is more readable?:
print(area_of_triangle(100, 20))
print(area_of_triangle(width = 100, height = 20))
# Ok, it is a simple math formula, but with more complex stuff
# you'd be like an elephant trying to clean its own shit from his back
# in a river of a creppy jungle

print(multi_add(4, 5, 10, 4, 15)) # function call with multi-undefined number of arguments
