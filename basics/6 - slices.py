
dummy_data = []
dummy_data = [1,2,3,4,5,6,7,8,9,10]

dummy_data[0] # 1
dummy_data[1] # 2
dummy_data[9] # 10

dummy_data[0:5] # [1, 2, 3, 4, 5]
dummy_data[2:5] # [3, 4, 5]
dummy_data[4:] # [5, 6, 7, 8, 9, 10]
dummy_data[:7] # [1, 2, 3, 4, 5, 6, 7]
dummy_data[2:7:2] # [3, 5, 7]
dummy_data[:] = range(100)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]
dummy_data[27:43:3] = (99,99,99,99,99,99)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 99, 28, 29, 99, 31, 32, 99, 34, 35, 99, 37, 38, 99, 40, 41, 99, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# replace some values
letters[2:5] = ['C', 'D', 'E'] # ['a', 'b', 'C', 'D', 'E', 'f', 'g']
# now remove them
letters[2:5] = [] # ['a', 'b', 'f', 'g']
# clear the list by replacing all the elements with an empty list
letters[:] = []


# If you need to modify the sequence you are iterating over while inside the loop(for example to duplicate selected items), it is recommended that you first make a copy. Iterating over a sequence does not implicitly make a copy. The slice notation makes this especially convenient:

words = ['cat', 'window', 'defenestrate']
# Loop over a slice copy of the entire list.
for w in words[:]:
	if len(w) > 6:
		words.insert(0, w)

# ['defenestrate', 'cat', 'window', 'defenestrate']
