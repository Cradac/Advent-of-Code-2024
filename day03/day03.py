import re

input = open(r"day03\\input.txt", "r")
input = input.readlines()

INSTRUCTION_PATTERN = r"(?:mul\(\d{1,3},\d{1,3}\))"
SUM_MULTIPLICATIONS = 0


def decipher_MUL(instruction: str):
    a, b = re.findall(r"(?:\d{1,3})", instruction)
    return int(a)*int(b)

for line in input:
    if line == '' or not line:
        continue
    matches = re.findall(INSTRUCTION_PATTERN, line)
    for match in matches:
        SUM_MULTIPLICATIONS += decipher_MUL(match)

print("Sum of Multiplications: (Star #1)")
print(SUM_MULTIPLICATIONS)

INSTRUCTION_PATTERN2 = r"(?:mul\(\d{1,3},\d{1,3}\))|(?:don't\(\))|(?:do\(\))"
SUM_MULTIPLICATIONS2 = 0
ENABLED_FLAG = True

for line in input:
    if line == '' or not line:
        continue
    matches = re.findall(INSTRUCTION_PATTERN2, line)
    for match in matches: 
        if match == "do()":
            ENABLED_FLAG = True
        elif match == "don't()":
            ENABLED_FLAG = False
        elif ENABLED_FLAG:
            SUM_MULTIPLICATIONS2 += decipher_MUL(match)
        else:
            #print("currently disabled")
            pass

print("Sum of Multiplications of enabled multiplications: (Star #2)")
print(SUM_MULTIPLICATIONS2)