import copy
import numpy as np

data = []
with open('input3.txt') as f:
	for line in f:
		data.append(line.strip())
data = np.array([list(i) for i in data])
print(data)

row_max = data.shape[0]
col_max = data.shape[1]
print(row_max, col_max)

positions = []
positions_proposed = []

for row,line in enumerate(data):
	for col,value in enumerate(line):
		if value=='#':
			positions.append([row,col])
print(positions)


def around_check(row, col):
	exist = False
	around = copy.deepcopy(data)
	around[row, col] = 'x'
	around = around[max(row-1,0):min(row,row_max), max(col-1,0):min(col,col_max)]
	if np.sum(around == '#') > 0:
		exist = True
	return exist
assert around_check(2,1)==True


def north_check(row, col):
	pass


print('give up!')