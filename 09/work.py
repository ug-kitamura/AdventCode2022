import numpy as np

data = np.loadtxt("input.txt", dtype='str')
print(data)

head = [0, 0]
tail = [0, 0]
tail_positions = [(0,0)]


def eval_touch(head, tail):
	isTouched = False
	if head[0]-1 <= tail[0] <= head[0]+1:
		if head[1]-1 <= tail[1] <= head[1]+1:
			isTouched = True
	return isTouched


def move(direction, head, tail):
	head_old = [i for i in head]

	if direction == 'L':
		head[0] -= 1
	elif direction == 'R':
		head[0] += 1
	elif direction == 'U':
		head[1] += 1
	elif direction == 'D':
		head[1] -= 1
	else:
		pass

	if eval_touch(head, tail) == False:
		tail = head_old

	return tail


for i in data:
	direction = i[0]
	times = int(i[1])

	for j in range(times):
		tail = move(direction, head, tail)
		tail_positions.append(tuple(tail))

print(f'part1: {len(set(tail_positions))}')
print(f'part2: give up!')

