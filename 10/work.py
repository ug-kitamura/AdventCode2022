import numpy as np

data = []
with open('input.txt') as f:
	for line in f:
		if line.startswith('noop'):
			data.append(['N', 0]) # no operatoin
		if line.startswith('addx'):
			value = line.strip().split(' ')[1]
			data.append(['A', value]) #add operation
			data.append(['W', 0]) #wait operation (same as no operation)
data = np.array(data)
print(data)

X = [1] + [0] * len(data)
for num, ope in enumerate(data):
	X[num+1] = X[num+1] + X[num]
	if ope[0] == 'N':
		pass
	elif ope[0] == 'W':
		pass
	elif ope[0] == 'A':
		X[num+2] += int(ope[1])

#print(X[20-1], X[60-1], X[100-1], X[140-1], X[180-1], X[220-1])
strength = 20*X[20-1] + 60*X[60-1] + 100*X[100-1] + 140*X[140-1] + 180*X[180-1] + 220*X[220-1]
print(f'part1: {strength}')

X.pop(-1)
CRT= ''
for i,j in enumerate(X):
	col = i%40
	if -1 <= (col - j) <= 1:
		CRT += '#'
	else:
		CRT += '.'
	if col == 39:
		CRT += '\n'

print('part2:')
print(CRT) #EHZFZHCZ
