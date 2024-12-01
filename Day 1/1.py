leftList = []
rightList = []
sum = 0

with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        left, right = line.split("   ")
        leftList.append(int(left))
        rightList.append(int(right))

leftListSorted = sorted(leftList)
rightListSorted = sorted(rightList)

for left, right in zip(leftListSorted, rightListSorted):
    sum += abs(left - right)

print(sum)