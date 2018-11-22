


def bling1(f):
    def wrap(text):
        print("****")
        f(text)
        print("****")
    return wrap


def first_hello(text):
    print(text)
first_hello = bling1(first_hello)
# this is a shorter way of doing
# what we did above
@bling1
def second_hello(text):
    print(text)


first_hello("First Hello World!")
print() # separator
second_hello("Second Hello World!")


print() # separator

def bling2(f):
    def wrap(text):
        print("~~~~")
        f(text)
        print("~~~~")
    return wrap

# the order is important:
@bling1
@bling2
def third_hello(text):
    print(text)
# third_hello = bling1(bling2(third_hello))
third_hello("Third Hello World")

print() # separator

# the order is important:
@bling2
@bling1
def fourth_hello(text):
    print(text)
# fourth_hello = bling2(bling1(fourth_hello))
fourth_hello("Fourth Hello Word")
