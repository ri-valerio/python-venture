

color = "Yellow" # this variable is global


def first_function():
    # it can't be because color is a global
    # variable and we can't access it like this
    print("Am I Painting the global var with", color)

try:
    first_function(color)
except:
    print("It wasn't possible! Get your Facts right!")


def second_function():
    color = "Green" # this variable is local
    print("Painting some local var to", color)
second_function()
print("But the global is still", color)


def third_function():
    global color
    color = "Red" # now we are changing the global variable we defined on line 3
    print("Changing the global to", color)
third_function()
print("Now the global is also", color)


def fourth_function():
    a = "Blue"
    def fifth_function():
        a = "Orange"
        print(a)
    fifth_function()
    print(a)
fourth_function()


def sixth_function():
    a = "Blue"
    def seventh_function():
        nonlocal a
        a = "Orange"
        print(a)
    seventh_function()
    print(a)
sixth_function()
