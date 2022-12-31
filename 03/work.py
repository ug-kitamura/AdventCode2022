import numpy as np

data = np.loadtxt("input.txt", dtype='str')
data = list(data)
print(data)


def alphabet_to_score(alphabet):
    if alphabet.islower() == True:
        score = ord(alphabet)-97+1
    else:
        score = ord(alphabet)-65+27
    return score


total_score = 0
for i in data:
    length = len(i)//2
    first  = i[:length]
    second = i[length:]
    common = set(first) & set(second)
    common = list(common)
    score = alphabet_to_score(common[0])
    total_score = total_score + score
    print(first, second, score, f'({common[0]})')

print(f'part1: {total_score}')


total_score = 0
for i in range(len(data)//3):
    data2 = data[i*3:i*3+3]
    print(data2)
    common = set(data2[0]) & set(data2[1]) & set(data2[2])
    common = list(common)
    score = alphabet_to_score(common[0])
    total_score = total_score + score
    print(score, f'({common[0]})')

print(f'part2: {total_score}')

