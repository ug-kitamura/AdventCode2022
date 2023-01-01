import numpy as np

data = np.loadtxt("input.txt", dtype='str')

stack = [
    """
    'ZN',
    'MCD',
    'P',
    """
    'GTRW',
    'GCHPMSVW',
    'CLTSGM',
    'JHDMWRF',
    'PQLHSWFJ',
    'PJDNFMS',
    'ZBDFGCSJ',
    'RTB',
    'HNWLC',
]
print(stack)


def move_stack(num, start, end):
    col1 = stack[start]
    col2 = stack[end]
    for i in range(num):
        col2 = col2 + col1[-1]
        col1 = col1[:-1]
    stack[start] = col1
    stack[end]   = col2


def move_stack2(num, start, end):
    col1 = stack[start]
    col2 = stack[end]
    col2 = col2 + col1[-num:]
    col1 = col1[:-num]
    stack[start] = col1
    stack[end]   = col2


input = []
for i in data:
    input.append([int(i[1]), int(i[3])-1, int(i[5])-1])


for i in input:
    num   = i[0]
    start = i[1]
    end   = i[2]
    move_stack2(num, start, end)
print(stack)


result = ''
for i in stack:
    result = result + i[-1]
print(result)

