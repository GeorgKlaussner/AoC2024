import numpy as np
sum = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        lineList = np.array([int(i) for i in line.split(" ")])

        diff = np.diff(lineList)
        if np.all(diff < 0) and np.all(diff >= -3) :
            sum += 1
        elif np.all(diff > 0) and np.all(diff <= 3) :
            sum += 1
        elif np.count_nonzero(diff >= 0) == 1 or np.count_nonzero(diff <= 0) == 1:
            sum += 1
print(sum)