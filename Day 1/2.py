import numpy as np

leftList = np.array([])
rightList = np.array([])
sum = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        left, right = line.split("   ")
        leftList = np.append(leftList, int(left))
        rightList = np.append(rightList, int(right))

for item in leftList:
    if item in rightList:
        factor = np.count_nonzero(rightList == item)
        sum += item * factor

print(sum)