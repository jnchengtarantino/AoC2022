import numpy as np
from collections import Counter, defaultdict
from functools import reduce, cache
from itertools import accumulate
from math import lcm
import re

# file = open("testinput.txt")
file = open("day16input.txt")

network = {}
flow = {}

lines = file.readlines()
for line in lines:
    line = line.strip().replace("; ", " ").replace("=", " ").replace(", ", " ").split(" ")
    label = line[1]
    network[label] = line[10:]
    if int(line[5]) > 0 : flow[label] = int(line[5])

def bfs(target: str, curr: str, depth: int, q: list, visited: list):
    if curr == target:
        return depth
    else:
        for child in network[curr]:
            if child not in visited and child not in q:
                q.append((child, depth + 1))
        
        visited.append(curr)
        next, nextDepth = q.pop(0)
        return bfs(target, next, nextDepth, q, visited)

@cache
def bfsWrapper(target, start):
    return bfs(target, start, 0, [], [])

@cache
def part1(tRemaining, unvisited=frozenset(flow.keys()), curr='AA', released=0,e=False):
    newUnvisited = frozenset(unvisited.difference({curr}))
    if curr in newUnvisited: newUnvisited.remove(curr)

    if tRemaining <= 0: return released
    if curr in flow.keys(): released += tRemaining * flow[curr]
    if len(newUnvisited) == 0: return released

    return max([part1(tRemaining-bfsWrapper(next,curr)-1, newUnvisited, next, released, e) for next in newUnvisited]
    + [part1(26, unvisited=newUnvisited) if e else 0])

# print(part1(30))
print(part1(26, e=True))
file.close()