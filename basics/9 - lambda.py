


def basic_function(a):
    return a + 2
print(basic_function(1))


same_with_lambda = lambda a: a + 2
print(same_with_lambda(1))


print() # separator


numbers = [1, 2, 3, 4, 5]
numbers = list(map(lambda x: x**2, numbers))
print(numbers)
