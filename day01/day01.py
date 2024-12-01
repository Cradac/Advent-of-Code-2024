input = open(r"day01\\input.txt", "r")
input = input.read().split('\n')

LISTL = []
LISTR = []

SUM_DISTANCE: int = 0

# sort input into two lists:
for line in input:
    if not line or line == "":
        continue
    left, right = line.split("   ")
    LISTL.append(int(left))
    LISTR.append(int(right))

# sort Lists
LISTL.sort(reverse=True)
LISTR.sort(reverse=True)

LISTL2 = LISTL.copy()
LISTR2 = LISTR.copy()

# calculating and popping
while len(LISTL) > 0 and len(LISTR) > 0:
    SUM_DISTANCE += abs(LISTL.pop() - LISTR.pop())

print("Sum of the Distance: (Star #1)")
print(SUM_DISTANCE)

# Star #2
SIMILARITY_SCORE: int = 0

for item in LISTL2:
    SIMILARITY_SCORE += item * LISTR2.count(item)

print("Similarity Score: (Star #2)")
print(SIMILARITY_SCORE)