input = open(r"day02\\input.txt", "r")
input = input.read().split('\n')
reports = [x.split(" ") for x in input]

SUM_SAFE_REPORTS = 0
# For Star #2
SUM_FIXED_REPORTS = 0

def check_increasing(report: list):
    direction = ""
    prev = int(report[0])
    curr = int(report[1])
    # I know this is an abomination, please don't come for me
    if prev < curr:
        direction = "INCREASING"
    elif prev > curr:
        direction = "DECREASING"
    else:
        return False
    for x in range(1, len(report)):
        curr = int(report[x])
        if direction == "INCREASING":
            if not prev < curr:
                return False
        if direction == "DECREASING":
            if not prev > curr:
                return False
        prev = curr
    return True

def check_safe_levels(report: list):
    # I'm still not sure if this is how you should handle looping through a list to compare neighbors...
    prev = report[0]
    for x in range(1, len(report)):
        curr = report[x]
        diff = abs(int(prev)-int(curr))
        if 1 <= diff <= 3:
            prev = curr
        else:
            return False
    return True



for report in reports:
    # fuck empty lines all my homies hate empty lines
    if report == ['']:
        continue
    # checking for the first time
    if check_increasing(report) & check_safe_levels(report):
        SUM_SAFE_REPORTS += 1
        #print("already perfect!")
    else:
        # check for the second time
        for x in range(len(report)):
            # get a copy to work on and try if popping every index once fixes the issue.
            working_copy = report.copy()
            popped = working_copy.pop(x)
            if check_increasing(working_copy) & check_safe_levels(working_copy):
                SUM_FIXED_REPORTS += 1
                #print("And now I'm fixed!")
                # we love a break in a for loop
                break



print("Sum of Safe Reports: (Star #1)")
print(SUM_SAFE_REPORTS)

print("Sum of Safe Reports with Problem Dampener: (Star #2)")
print(SUM_SAFE_REPORTS+SUM_FIXED_REPORTS)
