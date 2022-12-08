import numpy as np
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
# file = open("testinput.txt")
file = open("day8input.txt")

def score(target: int, x: list[int]):
    count = 0
    for n in x:
        count += 1
        if n >= target:
            break
    return count

initial = []
lines = file.readlines()
for line in lines:
    initial.append([int(x) for x in line.strip()])

map = np.array(initial)
scores = np.zeros_like(map)

# count = 0
for i in range(len(map)):
    for j in range(len(map[i])):
        # if map[i][j] > max(map[i,:j], default=-1) or map[i][j] > max(map[i,j+1:], default=-1) or map[i][j] > max(map[:i,j], default=-1) or map[i][j] > max(map[i+1:,j], default=-1):
        #     count += 1
        t = map[i][j]
        scores[i][j] = score(t, np.flip(map[i,:j])) * score(t, map[i,j+1:]) * score(t, np.flip(map[:i,j])) * score(t, map[i+1:,j])

# print(count)
print(np.max(scores))        

file.close()