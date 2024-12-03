import re
sum = 0

def mul(cmd):
    a, b = [int(i) for i in cmd.split(",")]
    return a * b

with open("input.txt") as f:
    for line in f.readlines():
        line = line.replace("\n", "")
        segments = line.split("don't")
        for segment in segments:
            segmentMatch = re.search(r'do\(\)', segment)
            if segmentMatch:
                pos, _ = segmentMatch.span()
                segmentString = segment[pos:]

                cmds = re.findall(r"mul\((\d+,\d+)\)", segmentString)
                for cmd in cmds:
                    sum += mul(cmd)
print(sum)