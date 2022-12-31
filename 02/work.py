total_score1 = 0
total_score2 = 0

with open('input.txt') as f:
    for line in f:
        line = line.strip()

        if line == 'A X':
            score = 4
        elif line == 'A Y':
            score = 8
        elif line == 'A Z':
            score = 3
        elif line == 'B X':
            score = 1
        elif line == 'B Y':
            score = 5
        elif line == 'B Z':
            score = 9
        elif line == 'C X':
            score = 7
        elif line == 'C Y':
            score = 2
        elif line == 'C Z':
            score = 6
        else:
            raise Exception('Error!')
        total_score1 = total_score1 + score

        if line == 'A X':
            score = 3
        elif line == 'A Y':
            score = 4
        elif line == 'A Z':
            score = 8
        elif line == 'B X':
            score = 1
        elif line == 'B Y':
            score = 5
        elif line == 'B Z':
            score = 9
        elif line == 'C X':
            score = 2
        elif line == 'C Y':
            score = 6
        elif line == 'C Z':
            score = 7
        else:
            raise Exception('Error!')
        total_score2 = total_score2 + score

print(f'part1: {total_score1}')
print(f'part2: {total_score2}')
