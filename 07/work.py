path = []
filelist = []
with open('input.txt') as f:
	for line in f:
		if line.startswith("$ cd /"):
			pass
		elif line.startswith("$ cd .."):
			path.pop(-1)
		elif line.startswith("$ cd"):
			dir = line.strip().split(' ')[2]
			path.append(dir)
		elif line.startswith("$ ls"):
			pass
		elif line.startswith("dir"):
			pass
		else:
			size = int(line.strip().split(' ')[0])
			name = line.strip().split(' ')[1]
			filelist.append(path + [size])


depth = 0
dir_dict = {}
while depth < 100:
	for file in filelist:
		size = file[-1]
		if len(file) - depth >= 2:
			dir = '/'.join(file[:depth+1])
			if dir in dir_dict:
				dir_dict[dir] = dir_dict[dir] + size
			else:
				dir_dict[dir] = size
	depth = depth + 1

print(dir_dict)


dir_size_total = 0
for dir_size in dir_dict.values():
	if dir_size <= 100000:
		dir_size_total = dir_size_total + dir_size

print(f'part1: {dir_size_total}')


root_size = 0
for file in filelist:
	size = file[-1]
	root_size = root_size + size

print(f'root size: {root_size}')


necessary_space = 30000000 - (70000000 - root_size)
print(f'necessary space: {necessary_space}')

values = list(dir_dict.values())
values.sort()
for i in values:
	if i > necessary_space:
		print(f'part2: {i}')
		break

