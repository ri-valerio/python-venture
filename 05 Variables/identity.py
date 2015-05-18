# inside the IDLE type:
"""

	>>> x = 42
	>>> x
	42
	>>> id(x)
	10456352
	>>> y = 42
	>>> id(y)
	10456352
	>>> x = 43
	>>> id(x)
	10456384
	>>> id(y)
	10456352
	>>> id(x)
	10456384
	>>> y = 43
	>>> id(y)
	10456384
	>>> x is y
	True
	>>> x == y
	True
	>>> x = dict(x = 42)
	>>> type(x)
	<class 'dict'>
	>>> x
	{'x': 42}
	>>> id(x)
	139785825869960
	>>> y = dict(x = 42)
	>>> id(y)
	139785825879944
	>>> x == y
	True
	>>> x is y
	False

"""
