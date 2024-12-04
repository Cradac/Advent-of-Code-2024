import re
from collections import defaultdict

input = open(r"day04\\input.txt", "r")
input = input.read().split('\n')

# PART #1

XMAS_PATTERN = r"(?=((XMAS)|(SAMX)))"
XMAS_COUNTER = 0

def check_pattern(line: str):
    return len(re.findall(XMAS_PATTERN, line))

# check horizontal
for line in input:
    XMAS_COUNTER += check_pattern(line)

# check vertical
# rotate Matrix 90° to the right
for line in zip(*input[::-1]):
    XMAS_COUNTER += check_pattern("".join(line))

# check diagonals
# I straight up ripped this from stackoverflow
def groups(data, func):
    grouping = defaultdict(list)
    for y in range(len(data)):
        for x in range(len(data[y])):
            grouping[func(x, y)].append(data[y][x])
    return list(map(grouping.get, sorted(grouping)))

# fdiag
for line in groups(input, lambda x, y: x + y):
    XMAS_COUNTER += check_pattern("".join(line))

# bdiag
for line in groups(input, lambda x, y: x - y):
    XMAS_COUNTER += check_pattern("".join(line))

print("Amount of XMAS in Input: (Star #1)")
print(XMAS_COUNTER)

# PART 2

X_MAS_COUNTER = 0

def check_for_XMAS_bdiag(center):
    if input[center[0]+1][center[1]+1] == 'M' and input[center[0]-1][center[1]-1] == 'S':
        return True
    elif input[center[0]+1][center[1]+1] == 'S' and input[center[0]-1][center[1]-1] == 'M':
        return True
    return False

def check_for_XMAS_fdiag(center):
    if input[center[0]+1][center[1]-1] == 'M' and input[center[0]-1][center[1]+1] == 'S':
        return True
    elif input[center[0]+1][center[1]-1] == 'S' and input[center[0]-1][center[1]+1] == 'M':
        return True
    return False

# iterate over matrix and find A's which are not on the outer lines:
for y in range(len(input)):
    if y == 0 or y == len(input)-1:
        continue
    for x in range(len(input[y])):
        if x == 0 or x == len(input[0])-1:
            continue
        if check_for_XMAS_bdiag([y,x]) and check_for_XMAS_fdiag([y,x]) and input[y][x] == 'A':
            X_MAS_COUNTER += 1

print("Amount of X-MAS in Input: (Star #2)")
print(X_MAS_COUNTER)