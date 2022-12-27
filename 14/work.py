"""
	air  : 0
	rock : 1
	sand : 2
	start: 9
"""

import numpy as np

part2 = True

data = []
with open('input.txt') as f:
	for line in f:
		path = [eval(i) for i in line.strip().split(' -> ')]
		data.append(path)
#print(data)

y_list = []
for i in data:
	for j in i:
		y_list.append(j[1])
y_max = max(y_list) + 2
#print(f'max y: {y_max}')

start_position = (500, 0)
map = np.zeros((1000, y_max+1))
map[start_position[0], start_position[1]] = 9


def set_rock(start, end):
	map[start[0], start[1]] = 1
	map[end[0]  , end[1]  ] = 1

	if start[0] == end[0]:
		map[start[0], min(start[1],end[1]):max(start[1],end[1])] = 1
	if start[1] == end[1]:
		map[min(start[0],end[0]):max(start[0],end[0]), start[1]] = 1


def check_next(next):
	x = next[0]
	y = next[1]
	if map[x, y] == 0:
		isAir = True
	else:
		isAir = False
	return isAir


for i in data:
	for j in range(len(i)-1):
		set_rock(i[j], i[j+1])
if part2 == True:
	set_rock((0,y_max), (999,y_max))

print(map[start_position[0]-12:start_position[0]+12,0:y_max+1].T)
print()


rock = 0
isCompleted=False
while isCompleted==False:
	current = start_position
	isStopped = False
	while isStopped==False:
		if current[1] >=y_max:
			isCompleted = True
			break
		next = [current[0], current[1]+1]
		if check_next(next) == True:
			current = next
			continue
		else:
			next = [current[0]-1, current[1]+1]
			if check_next(next) == True:
				current = next
				continue
			else:
				next = [current[0]+1, current[1]+1]
				if check_next(next) == True:
					current = next
					continue
				else:
					map[current[0], current[1]] = 2
					rock += 1
					isStopped = True
					if current == start_position:
						isCompleted = True

print(map[start_position[0]-12:start_position[0]+12,0:y_max+1].T)
print()

if part2 == True:
	print(f'part2: {rock}')
else:
	print(f'part1: {rock}')
