#!/usr/bin/python3


# looping lines from a file
with open('poema.txt') as file:
	for line in file:
		print(line, end="")

print() # separator

print("looping a range", end=": ")
for x in range(1,10):
	print(x, end=" ")

print() # separator

print("looping a tuple", end=": ")
for x in (1,10):
	print(x, end=" ")

print() # separator

print("looping a set", end=": ")
for x in {1, 2, 3}:
	print(x, end=" ")

print() # separator

print("looping a list", end=": ")
for x in [1, 2, 3]:
	print(x, end=" ")

print() # separator

print("looping a sequence of numbers", end=": ")
for x in 1, 2, 3:
	print(x, end=" ")

print() # separator

print("looping a sequence of characters", end=": ")
for x in 'N', 'S', 'A':
	print(x, end=" ")

print() # separator

print("looping each character in a string", end=": ")
for x in "bazinga":
	print(x, end=" ")

print() # separator

# list comprehenesions
ma_list_yo = [1, 2, 3, 4, 5, 6]
print([x**2 for x in ma_list_yo])
print([x**2 for x in ma_list_yo if x % 2 == 0])

print()  # separator

# we can use else in "while" and "for" loops
# to perform something when it ends or not breaks
s = 'thisx isx ax string!x moxthexrfuxckxer!\n'
for c in s:
	if c == 'x':
		continue
	# if c == 'm': break
	print(c, end='')
else:
	print("This only prints without the BREAK!")

a = 0
while a < 10:
	print(a, end=' ')
	a += 1
else:
	print("done =)")

for each_char in "bazinga":
		print(each_char, end='')
else:
	print(" - done =)")


print()  # separator

x, y = 0, 0

while y < 5:
    print(y)
    y += 1  # y = y + 1

print()  # separator

# define a for loop
for x in range(5, 10):
    print(x)

print()  # separator

days_of_the_week = ["Mon", "Tue", "Wed", "Thu",
                    "Fri", "Sat", "Sun"]
# use a for loop over a collection
for each_day in days_of_the_week:
    print(each_day)
# using the enumerate() function to get index
for i, day in enumerate(days_of_the_week):
    print(i, day)

print()  # separator

# use the break and continue statements
for x in range(5, 10):
    # if (x == 7): break
    if (x % 2 == 0):
    	continue
    print(x)

print()  # separator

"""Exemplo para demonstrar que a atribuição
de variáveis pode dar origens a erros lógicos
"""
a, b = 0, 1
while b < 50:
    print(b)
    a, b = b, a + b
    # it is not the same if we use the attribution below:
    # a = b
    # b = a + b
