import numpy as np
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
from math import lcm
# file = open("testinput.txt")
file = open("day14input.txt")

filled = set()
lowestY = 9999

lines = file.readlines()
for line in lines:
    corners = line.split("->")
    corners = [c.strip().split(",") for c in corners]

    for i in range(1, len(corners)):
        if corners[i][0] == corners[i-1][0]:
            aaa = [ (int(corners[i][0]),x) for x in range(int(corners[i][1]), int(corners[i-1][1]) + 1)] or [ (int(corners[i][0]),x) for x in range(int(corners[i-1][1]), int(corners[i][1]) + 1) ]
            filled.update(aaa)
        elif corners[i][1] == corners[i-1][1]:
            bbb = [ (x,int(corners[i][1])) for x in range(int(corners[i][0]), int(corners[i-1][0]) + 1)] or [ (x,int(corners[i][1])) for x in range(int(corners[i-1][0]), int(corners[i][0]) + 1)]
            filled.update(bbb)

lowest = max([coord[1] for coord in filled])
filled.update((x, lowest+2) for x in range(0,1000))
ctr = 0

while True:
    x, y = 500, 0
    # while y <= lowest:
    while (500, 0) not in filled:
        cases = [0,-1,1]
        for case in cases:
            if (x+case,y+1) not in filled:
                x += case
                y += 1
                break
        else:
            filled.add((x,y))
            ctr += 1
            break
    else:
        break

print(ctr)    
        
file.close()