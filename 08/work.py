import numpy as np

data = np.loadtxt("input.txt", dtype='str')
data = np.array([list(i) for i in data])
print(data)

row_size = data.shape[0]
col_size = data.shape[1]


def evaluate_part1(value, target):
	eval = True
	if len(target) == 0:
		pass
	else:
		for i in target:
			if int(i) >= int(value):
				eval = False
	return eval


def evaluate_part2(value, target):
	eval = 0
	if len(target) == 0:
		pass
	else:
		for i,j in enumerate(target):
			eval = i+1
			if int(j) >= int(value):
				break
	return eval


count = 0
score_list = []
for row in range(row_size):
	for col in range(col_size):
		value = data[ row   , col   ]
		left  = data[ row   ,:col   ]
		right = data[ row   , col+1:]
		up    = data[:row   , col   ]
		down  = data[ row+1:, col   ]

		if any([evaluate_part1(value, left), evaluate_part1(value, right), evaluate_part1(value, up), evaluate_part1(value, down)]):
			count = count + 1

		score = evaluate_part2(value, left[::-1]) * evaluate_part2(value, right) * evaluate_part2(value, up[::-1]) * evaluate_part2(value, down)
		score_list.append(score)


print(f'part1: {count}')
print(f'part2: {max(score_list)}')

