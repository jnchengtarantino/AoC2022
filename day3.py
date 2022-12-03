import numpy as np
from collections import Counter
import itertools
# file = open("testinput.txt")
file = open("day3input.txt")

def value(c):
    if ord(c) < 93:
        return ord(c) - 38
    else:
        return ord(c) - 96

res = 0
group = []
lines = file.readlines()
for lineNum, line in enumerate(lines):
    line = line.strip()

    # part 1
    # s = len(line)//2
    # c1 = line[0:s]
    # c2 = line[s:]
    # same = set([c for c in c1 if c in c2])
    # for x in same: 
    #     res += value(x)

    # part 2
    group.append(line)
    if lineNum%3 == 2:
        e1,e2,e3 = group
        same = set([c for c in e1 if c in e2 and c in e3])
        for x in same:
            res += value(x)
        print(same)
        group = []
        
print(res)
        
file.close()