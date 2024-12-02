import numpy as np
sum = 0

def isDamper():
    for index in range(len(input)):
        inputRed = np.delete(input, index)
        diff = np.diff(inputRed)
        if np.all(diff < 0) and np.all(diff >= -3):
            return True
        elif np.all(diff > 0) and np.all(diff <= 3):
            return True
    return False

with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        lineList = np.array([int(i) for i in line.split(" ")])

        diff = np.diff(lineList)
        if np.all(diff < 0) and np.all(diff >= -3) :
            sum += 1
        elif np.all(diff > 0) and np.all(diff <= 3) :
            sum += 1
        elif isDamper(lineList):
            sum += 1

print(sum)