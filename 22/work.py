import numpy as np

data = []
with open('input.txt') as f:
	for line in f:
		line = line.replace(' ', '0')
		data.append(line.strip())

start_row = 0
start_col = data[0].find('.')
start_dir = 'r'

data1 = data[:-2]
col_max = max([len(i) for i in data1])
data1 = [i+'0'*(col_max-len(i)) for i in data1]
data1 = np.array([list(i) for i in data1])
row_max = len(data1)
print(data1)

data2 = data[-1]
data2 = data2.replace('L', ' L ')
data2 = data2.replace('R', ' R ')
data2 = data2.split(' ')
print(data2)


def check_out(row, col):
	if row<0 or row>=row_max:
		isOut = True
		return isOut
	if col<0 or col>=col_max:
		isOut = True
		return isOut
	if data1[row, col] == '0':
		isOut = True
	else:
		isOut = False
	return isOut


def check_wall(row, col):
	if data1[row, col] == '#':
		isWall = True
	else:
		isWall = False
	return isWall


def jump(row, col, dir):
	if dir == 'r':
		row_next = row
		index = [i for i,j in enumerate(data1[row,:]) if j=='.' or j=='#']
		col_next = index[0]
	elif dir == 'l':
		row_next = row
		index = [i for i,j in enumerate(data1[row,:]) if j=='.' or j=='#']
		col_next = index[-1]
	elif dir == 'd':
		col_next = col
		index = [i for i,j in enumerate(data1[:,col]) if j=='.' or j=='#']
		row_next = index[0]
	elif dir == 'u':
		col_next = col
		index = [i for i,j in enumerate(data1[:,col]) if j=='.' or j=='#']
		row_next = index[-1]
	else:
		raise Exception('Error!')
	return row_next, col_next


def forward(row, col, dir):
	if dir == 'r':
		row_next = row
		col_next = col+1
	elif dir == 'd':
		row_next = row+1
		col_next = col
	elif dir == 'l':
		row_next = row
		col_next = col-1
	elif dir == 'u':
		row_next = row-1
		col_next = col
	else:
		raise Exception('Error!')
	if check_out(row_next, col_next) == True:
		row_next, col_next = jump(row_next, col_next, dir)
	if check_wall(row_next, col_next) == True:
		row_next = row
		col_next = col
	return row_next, col_next


def turn(dir, clock):
	dirs = 'rdlu'
	index = dirs.find(dir)
	if clock == 'L':
		dir_next = dirs[index-1]
	elif clock == 'R':
		dir_next = dirs[(index+1)%len(dirs)]
	else:
		raise Exception('Error!')
	return dir_next


def calc_pass(row, col, dir):
	dir_score = {
		'r':0,
		'd':1,
		'l':2,
		'u':3,
	}
	password = 1000*(row+1) + 4*(col+1) + dir_score[dir]
	return password


row = start_row
col = start_col
dir = start_dir

for i in data2:
	if i.isdigit() == True:
		num = int(i)
		for j in range(num):
			row, col = forward(row, col, dir)
	else:
		clock = i
		dir = turn(dir, clock)

password = calc_pass(row, col, dir)
print(f'part1: {password}')
print('part2: give up!')

