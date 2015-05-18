# type that inside IDLE

"""
	>>> 5
	5
	>>> 0b0101
	5
	>>> def to_binary(n): print("{:08b}".format(n))
	>>> to_binary(5)
	00000101
	>>> to_binary(5)
	00000101
	>>> x, y = 0x55, 0xaa
	>>> x
	85
	>>> y
	170
	>>> to_binary(x)
	01010101
	>>> to_binary(y)
	10101010
	>>> to_binary(x | y)
	11111111
	>>> to_binary(x & y)
	00000000
	>>> to_binary(x ^ y)
	11111111
	>>> to_binary(x ^ 0xff)
	10101010
	>>> to_binary(x << 4)
	10101010000
	>>> to_binary(x >> 4)
	00000101
	>>> to_binary(~ x)
	-1010110

"""
