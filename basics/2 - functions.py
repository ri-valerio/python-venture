

def func1():
    print("I am a function")
func1()
# will print something and then prints "None"
# because the function doesn't return anything
print(func1())
# print the address location of the function object
print(func1)


# function that takes arguments
def func2(arg1, arg2):
    print(arg1, arg2)
func2(10, 20)
# will print something and then prints "None" again
# because the function doesn't return anything
print(func2(10, 20))


# function that returns a value
def cube(x):
    return x*x*x# or x**3
print(cube(3))


# function with default value for an argument
def power(num, x=1):
    return num ** x
print(power(2))
print(power(2, 3))
# reversing the order of the paramaters in
# respect to the order of the arguments definition,
# but yet, because we define the name of them,
# they will be correctly associated
# within the function itself
print(power(x=3, num=2))


# function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result
# function call with multi-undefined number of arguments
print(multi_add(4, 5, 10, 4, 15))


# function with named parameters
def area_of_triangle(width=0, height=0):
    return width * height / 2
# Which do you think is more readable?:
print(area_of_triangle(100, 20))
print(area_of_triangle(width=100, height=20))


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        # the "in" keyword tests whether or not
        # a sequence contains a certain value.
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# giving only the mandatory argument:
ask_ok('Do you really want to quit?')
# giving one of the optional arguments:
ask_ok('OK to overwrite the file?', 2)
# or even giving all arguments:
ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


# attention the "None" keyword is awesome
def testfunc(a, b=None, c=4):
    if b is None:
        print("How cool is that?")

    print('This is a test function', a, b, c)
testfunc(2)
testfunc(2, 3)
testfunc(2, 5, 7)


def my_awesome_function(a=7):
    for i in range(a, 10):
        print(i, end="")
    print()
my_awesome_function(2)
my_awesome_function()
my_awesome_function(4)


def my_extended_args_function(*args):
    print(args)
my_extended_args_function(1, 2, "it's sunny", 4)
# or call the function like this:
yupi = 1, 2, "it's sunny", 4
my_extended_args_function(*yupi)


def my_kwargs_function(**kwargs):
    print(kwargs['one'], kwargs['two'])
my_kwargs_function(one=1, two=2, three=3)
# or call the function like this:
schoobidoo = {0: 1, 1: 2, "weather": "it's sunny", "last": 4}
my_kwargs_function(**schoobidoo)


def my_all_args_and_kwargs_function(this, that, *args, **kwargs):
    print(this, that, args, kwargs["bazinga"], kwargs["scorpion"])
my_all_args_and_kwargs_function( 1, 2, 7, 8, 9, bazinga="sheldon", scorpion="on")


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Function annotations are completely optional metadata
#  information about the types used by user-defined functions
# (see PEP 484 for more information).
def fucking_sweet(ham: str, eggs: str='eggs') -> str:
    print("Annotations:", fucking_sweet.__annotations__)
    print("Arguments:", ham, eggs)
    return ham + ' and ' + eggs
fucking_sweet(ham='spam')
