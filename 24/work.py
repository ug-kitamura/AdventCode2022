import copy
import numpy as np

data = []
with open('input.txt') as f:
	for line in f:
		data.append(line.strip())
data = np.array([list(i) for i in data], dtype=object)
print(data)

row_max = data.shape[0]-1
col_max = data.shape[1]-1


def next_blizzard(row, col, dir):
	row_next = row
	col_next = col
	if dir == '>':
		if col+1 == col_max:
			col_next = 1
		else:
			col_next = col+1
	if dir == '<':
		if col-1 == 0:
			col_next = col_max-1
		else:
			col_next = col-1
	if dir == '^':
		if row-1 == 0:
			row_next = row_max-1
		else:
			row_next = row-1
	if dir == 'v':
		if row+1 == row_max:
			row_next = 1
		else:
			row_next = row+1
	return row_next, col_next


def next_map(data):
	next = copy.deepcopy(data)
	next[1:-1,1:-1] = '.'
	for row, line in enumerate(data):
		for col, dir in enumerate(line):
			for d in list(dir):
				if d!='#' and d!='.':
					row_next, col_next = next_blizzard(row, col, d)
					if next[row_next, col_next] == '.':
						next[row_next, col_next] = d
					elif next[row_next, col_next] == '#':
						next[row_next, col_next] = d
					else:
						next[row_next, col_next] = next[row_next, col_next] + d
	return next


def path_check(data, position_list):
	path = []
	for position in position_list:
		row  = position[0]
		col  = position[1]

		if data[row, col] == '.':
			path.append((row, col))
		if row+1 <= row_max:
			if data[row+1, col] == '.':
				path.append((row+1, col))
		if row-1 >= 0:
			if data[row-1, col] == '.':
				path.append((row-1, col))
		if col+1 <= col_max:
			if data[row, col+1] == '.':
				path.append((row, col+1))
		if col-1 >= 0:
			if data[row, col-1] == '.':
				path.append((row, col-1))

	path = list(set(path))
	print(path)
	return path


minute  = 0
start   = (0, 1)
goal    = (row_max, col_max-1)
current = copy.deepcopy(data)

path = [start]
while goal not in path:
	minute += 1
	current = next_map(current)
	print(minute)
	print(current)
	path = path_check(current, path)
min1 = minute

path = [goal]
while start not in path:
	minute += 1
	current = next_map(current)
	print(minute)
	print(current)
	path = path_check(current, path)
min2 = minute

path = [start]
while goal not in path:
	minute += 1
	current = next_map(current)
	print(minute)
	print(current)
	path = path_check(current, path)
min3 = minute

print(f'part1 {min1}')
print(f'part2 {min3} ({min1}->{min2-min1}->{min3-min2})')

