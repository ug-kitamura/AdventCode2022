data  = []
data2 = []
data3 = []

with open('input.txt') as f:
    for line in f:
        line = line.strip()
        if line=="":
            data2.append(data)
            data = []
        else:
            line = int(line)
            data.append(line)
    data2.append(data)

for i in data2:
    data3.append(sum(i))

print(f'part1: {max(data3)}')

max3 = 0
for i in range(3):
    max3 = max3 + max(data3)
    data3.remove(max(data3))

print(f'part2: {max3}')
