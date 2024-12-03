import re
sum = 0

def mul(cmd):
    a, b = [int(i) for i in cmd.split(",")]
    return a * b

with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        cmds = re.findall(r"mul\((\d+,\d+)\)", line)
        for cmd in cmds:
            sum += mul(cmd)
print(sum)