import numpy as np

data = np.loadtxt("input2.txt", dtype='str')
data = np.array([list(i) for i in data])

row_size = data.shape[0]
col_size = data.shape[1]
print(row_size, col_size)

start = [np.where(data=='S')[0][0], np.where(data=='S')[1][0]]
end   = [np.where(data=='E')[0][0], np.where(data=='E')[1][0]]
print(start, end)

data = np.where(data=='S', 'a', data)
data = np.where(data=='E', 'z', data)
data = [[ord(j)-ord('a') for j in i] for i in data]
data = np.array(data)
print(data)


def move(row, col, dir):
	next_position = [row, col]
	if dir=='left':
		if col-1 >= 0:
			if -1 <= data[row:col-1] - data[row:col] <= 1:
				if [row, col-1] not in positions_list:
					next_position = [row, col-1]
	if dir=='right':
		if col+1 <= col_size:
			if -1 <= data[row:col+1] - data[row:col] <= 1:
				if [row, col+1] not in positions_list:
					next_position = [row, col+1]
	if dir=='up':
		if row-1 >= 0:
			if -1 <= data[row-1:col] - data[row:col] <= 1:
				if [row-1, col] not in positions_list:
					next_position = [row-1, col]
	if dir=='down':
		if row+1 <= row_size:
			if -1 <= data[row+1:col] - data[row:col] <= 1:
				if [row+1, col] not in positions_list:
					next_position = [row+1, col]
	return next_position


positions_list = [start]
next_positions_list = []
step = 0

while True:
	print('give up!')
	"""
	for position in positions_list:
		row = position[0]
		col = position[1]

		for dir in ['left', 'right', 'up', 'down']:
			next_position = move(row, col, 'left')
			next_positions_list.append(next_position)

		print(next_positions_list)
		positions_list = [i for i in next_positions_list]
		next_positions_list = []

	step += 1
	"""

