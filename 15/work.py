import numpy as np

#y_target = 12
y_target = 2000000
checked_x_list = []


data = []
with open('input.txt') as f:
	for line in f:
		split = line.strip().split(' ')
		s_x = int(split[2][:-1].split('=')[-1])
		s_y = int(split[3][:-1].split('=')[-1])
		b_x = int(split[8][:-1].split('=')[-1])
		b_y = int(split[9].split('=')[-1])
		data.append([[s_x, s_y], [b_x, b_y]])
print(data)
print()


def calc_distance(s, b):
	distance = abs(s[0]-b[0]) + abs(s[1]-b[1])
	return distance
assert calc_distance([8,7],[2,10]) == 9


def check(sensor, distance, y_target):
	s_x = sensor[0]
	s_y = sensor[1]
	x_offset = distance - abs(y_target - s_y)
	x_list = [(i + s_x - x_offset) for i in range(x_offset * 2 + 1)]
	checked_x_list.extend(x_list)
	return x_list
assert check([5, 2], 10, 10)==[3,4,5,6,7]
assert check([8, 7],  9, 10)==[2,3,4,5,6,7,8,9,10,11,12,13,14]


for i in data:
	sensor = i[0]
	beacon = i[1]
	distance = calc_distance(sensor, beacon)
	check(sensor, distance, y_target)
	checked_x_list = list(set(checked_x_list))
	checked_x_list.sort()
	if (sensor[1] == y_target):
		checked_x_list.remove(sensor[0])
	if (beacon[1] == y_target):
		checked_x_list.remove(beacon[0])

#print(checked_x_list)
print(f'part1: {len(checked_x_list)}')
print('part2: give up!')
