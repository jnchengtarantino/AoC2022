import numpy as np
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
from math import lcm
# file = open("testinput.txt")
file = open("day12input.txt")

init = []
s = None
e = None

lines = file.readlines()
for i, line in enumerate(lines):
    if 'S' in line: s = (i, line.index('S'))
    if 'E' in line: e = (i, line.index('E'))
    init.append([c for c in line.strip().replace('S', 'a').replace('E', 'z')])

map = np.array(init)
steps = np.ones_like(map, dtype=int) * 3000
visited = set()

# q = [s]
# steps[s] = 0
# while q and e not in visited:
#     qSteps = [steps[n] for n in q]
#     x, y = q.pop(qSteps.index(min(qSteps)))
#     cases = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
#     for i, j in cases:
#         if 0 <= i < len(map) and 0 <= j < len(map[0]) and (i,j) not in visited and ord(map[i, j]) - ord(map[x, y]) <= 1:
#             steps[i, j] = min(steps[i,j], steps[x, y] + 1)
#             if (i,j) not in q: q.append((i, j))
#     visited.add((x, y))
# print(steps[e])

q = [e]
steps[e] = 0
while q:
    qSteps = [steps[n] for n in q]
    x, y = q.pop(qSteps.index(min(qSteps)))
    cases = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
    for i, j in cases:
        if 0 <= i < len(map) and 0 <= j < len(map[0]) and (i,j) not in visited and ord(map[x, y]) - ord(map[i, j]) <= 1:
            steps[i, j] = min(steps[i,j], steps[x, y] + 1)
            if (i,j) not in q: q.append((i, j))
    visited.add((x, y))

aSteps = []
for(i, j) in np.ndindex(map.shape):
    if map[i,j] == 'a': aSteps.append(steps[i,j])
print(min(aSteps))
file.close()