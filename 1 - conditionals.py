#!/usr/bin/python3

"""There can be zero or more elif parts, and the else part is optional. The keyword ‘elif’ is short for ‘else if’, and is useful to avoid excessive indentation. An if … elif … elif … sequence is a substitute for the switch or case statements found in other languages.
"""


a, b, z, PI = 0, 1, 1000, 3.14

if 0 or False or None or () or [] or {} or "" or "  ".strip():
	print("All of that was False! So it won't print!")

if 7 and z and PI and True and (4) and [5] and {6} and "hello":
	print("All of that was True! So it will print!")

print() # separator

if a < b:
	print("a is < than b")
elif a == b:
	print("a is == to b")
elif a > b:
	print("a is > than b")

print() # separator

is_a_less_than_b = "a is <= than b" if a < b or a == b \
					else "a is > than b"
print(is_a_less_than_b)
