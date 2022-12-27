import numpy as np

data  = np.loadtxt("input.txt", dtype='str')
data  = [eval(i) for i in data]


def compare(left, right):
	result = None
	if (type(left) is int) and (type(right) is int):
		result = compare_integers(left, right)
	elif (type(left) is list) and (type(right) is list):
		result = compare_lists(left, right)
	elif (type(left) is int) and (type(right) is list):
		left = [left]
		result = compare_lists(left, right)
	elif (type(left) is list) and (type(right) is int):
		right = [right]
		result = compare_lists(left, right)
	else:
		raise Exception('Error!')
	return result


def compare_integers(left, right):
	if left < right:
		return True
	if left > right:
		return False
	if left == right:
		return None


def compare_lists(left, right):
	min_size = min(len(left), len(right))
	for i in range(min_size):
		result = compare(left[i], right[i])
		if result == True:
			return True
		elif result == False:
			return False
		elif result == None:
			continue
		else:
			raise Exception('Error!')

	if len(left) < len(right):
		return True
	if len(left) > len(right):
		return False
	if len(left) == len(right):
		return None


assert compare_lists([1,1,3,1,1], [1,1,5,1,1]) == True
assert compare_lists([[1],[2,3,4]], [[1],4]) == True
assert compare_lists([9], [[8,7,6]]) == False
assert compare_lists([[4,4],4,4], [[4,4],4,4,4]) == True
assert compare_lists([7,7,7,7], [7,7,7]) == False
assert compare_lists([], [3]) == True
assert compare_lists([[[]]], [[]]) == False
assert compare_lists([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]) == False


score = 0
left_list  = data[::2]
right_list = data[1::2]
for i, (left, right) in enumerate(zip(left_list, right_list)):
	result = compare_lists(left, right)
	print(i+1, result, left, right)
	if result == True:
		score += i+1

print(f'part1: {score}')
print()


#########################################

data.extend([[2], [6]])
for i in range(len(data)):
	for j in range(len(data)-1):
		left  = data[j]
		right = data[j+1]
		result = compare_lists(left, right)
		if result == False:
			data[j]   = right
			data[j+1] = left

score = 1
for i,j in enumerate(data):
	print(i+1, j)
	if j == [2]:
		score *= i+1
	if j == [6]:
		score *= i+1

print(f'part2: {score}')

