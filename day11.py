import numpy as np
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
from math import lcm
# file = open("testinput.txt")
file = open("day11input.txt")

def parseOp(op):
    _, o = op.split("=")
    match o.strip().split(" "):
        case 'old', '*', 'old': return lambda old: old*old
        case 'old', '*', x: return lambda old: old * int(x)
        case 'old', '+', x: return lambda old: old + int(x)
        case _: print("parse error: " + op)

def testTarget(w, args):
    if w % args[0] == 0:
        return args[1] 
    else:
        return args[2]

items = []
ops = []
tests = []
counts = []

currMonkey = []
lines = file.readlines()
for line in lines:
    if line.strip() == '':
        _, startItems = currMonkey[1].split(":")
        items.append([int(i) for i in startItems.split(",")])
        ops.append(currMonkey[2])
        tests.append((int(currMonkey[3].strip().split(" ")[-1]), int(currMonkey[4].strip().split(" ")[-1]), int(currMonkey[5].strip().split(" ")[-1]))) 
        counts.append(0)
        currMonkey = []
    else:
        currMonkey.append(line)

divs = [t[0] for t in tests]
mod = lcm(*divs)

for _ in range(10000):
    for i in range(len(counts)):
        while items[i]:
            w = items[i].pop(0)
            w = parseOp(ops[i])(w) % mod
            target = testTarget(w, tests[i])
            items[target].append(w)
            counts[i] += 1
        
countsSorted = sorted(counts)
print(countsSorted[-1] * countsSorted[-2])
file.close()