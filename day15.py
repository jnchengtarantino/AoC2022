import numpy as np
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
from math import lcm
import re

# file = open("testinput.txt")
file = open("day15input.txt")

sensors = []
# beacons = []

lines = file.readlines()
for line in lines:
    sx, sy, bx, by = [int(i) for i in re.findall("-?[0-9]+", line.strip())]
    sensors.append((sx, sy, abs(bx - sx) + abs(by-sy)))
    # beacons.append((bx, by))

# yTarget = 2000000
# yTarget = 10
# occ = set()
# for x, y, r in sensors:
    # dx = r - abs(y-yTarget)
    # if dx >= 0:
        # occ.update(range(x-dx,x+dx+1))
# print(len(occ - set([b[0] for b in beacons if b[1] == yTarget])))


# maxSize = 20
maxSize = 4000000
yCoverage = [[] for _ in range(maxSize+1)]
for x, y, r in sensors:
    print("sensor: " + str(x) +"," + str(y))
    for j in range(max(0, y-r), min(maxSize, y+r+1)):
        dx = r - abs(y-j)
        yCoverage[j].append((max(0, x-dx), min(maxSize, x+dx)))

def while_contiguous(yCoverage):
    for j in range(len(yCoverage)):
        if j % 10000 == 0: print(j)
        sortedRanges = sorted(yCoverage[j])
        maxRight = -1
        for r in sortedRanges:
            if r[0] > maxRight + 1:
                return (maxRight+1, j)
            else:
                maxRight = max(maxRight, r[1])
        else:
            if maxRight < maxSize:
                return (maxRight + 1, j)

xRes, yRes = while_contiguous(yCoverage)
print(str(xRes) + ", " + str(yRes) + " : " +str(xRes*4000000 + yRes))

file.close()