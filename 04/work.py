import numpy as np

data = np.loadtxt("input.txt", dtype='str')
data = list(data)
print(data)

score  = 0
score2 = 0
for i in data:
    data = i.split(',')

    pair1_start = int(data[0].split('-')[0])
    pair1_end   = int(data[0].split('-')[1])

    pair2_start = int(data[1].split('-')[0])
    pair2_end   = int(data[1].split('-')[1])

    pair1 = set(range(pair1_start, pair1_end+1))
    pair2 = set(range(pair2_start, pair2_end+1))

    if (pair1<pair2) == True:
        score += 1
    elif (pair1>pair2) == True:
        score += 1
    elif pair1 == pair2:
        score += 1
    else:
        pass

    if pair1.isdisjoint(pair2) == False:
        score2 += 1
    else:
        pass
    #print(data, pair1_start, pair1_end, pair2_start, pair2_end, pair1, pair2)

print(f'part1: {score}')
print(f'part2: {score2}')
