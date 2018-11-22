
s0 = "this is the first string"
print(s0)
print(len(s0))
print(s0[2:7]) # from 2 to 6 - because 7 will not appear

# ascii special chars
s1 = "this is\n the second string"
print(s1)

# "raw" string
s2 = r"this is\n the third string"
print(s2)

n = 2
# obsolete way of printing
s3 = "this print is obsolete %d me dude!" % n
print(s3)
# new and best practice way
s4 = "print the number {} dude!".format(n)
print(s4)

s5 = f"print the number {n} again!"
print(s5)
# the "\" character does the same like c macros
# this is mostly used in "doc strings"
s5 = """\
this is a fucking
huge string that
I can break into
many lines as I like...
"""
print(s5)

name = "Froddo"
print(f"He said his name is {name!r}.")
print(f"He said his name is {repr(name)}.")  # repr() is equivalent to !r

width = 10
precision = 4
import decimal
value = decimal.Decimal("12.34567")
print(f"result: {value:{width}.{precision}}")  # nested fields

import datetime
today = datetime.datetime(year=2017, month=1, day=27)
print(f"{today:%B %d, %Y}")  # using date format specifier

number = 1024
print(f"{number:#0x}")  # using integer format specifier
