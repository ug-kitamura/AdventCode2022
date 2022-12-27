data = {}
with open('input.txt') as f:
	for line in f:
		split = line.strip().split(' ')
		monkey = split[0][:-1]
		if len(split) == 2:
			number = int(split[1])
			data[monkey] = [number]
		else:
			input1 = split[1]
			input2 = split[3]
			operation = split[2]
			data[monkey] = [input1, input2, operation]

def yell(monkey):
	if len(data[monkey]) == 1:
		number = data[monkey][0]
		return number
	else:
		input1, input2, operation = data[monkey]
		if operation == '+':
			return yell(input1) + yell(input2)
		elif operation == '-':
			return yell(input1) - yell(input2)
		elif operation == '*':
			return yell(input1) * yell(input2)
		elif operation == '/':
			return yell(input1) // yell(input2)
		else:
			raise Exception('Error!')

for key in data.keys():
	print(key, data[key])
print()
print(f"part1: {yell('root')}")

#data['humn'][0] = 0
data['humn'][0] = 3469704900000
monkey1 = data['root'][0]
monkey2 = data['root'][1]
while yell(monkey1)!=yell(monkey2):
	data['humn'][0] += 1

print(f"part2: {data['humn'][0]}")
