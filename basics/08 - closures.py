


def hello():
    counter = 0
    def friend():
        nonlocal counter
        counter += 1
        print(counter)
    return friend

f = hello()
f()
f()
f()

print() # separator

g = hello()
g()
g()

print()  # separator

f()
