import numpy as np
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
# file = open("testinput.txt")
file = open("day10input.txt")

x = [1]
res = []  

lines = file.readlines()
for line in lines:
    match line.strip().split(" "):
        case ["noop"]: x.append(0)
        case 'addx', val: x.extend([0,int(val)])

for i, val in enumerate(accumulate(x), 1):
    # if i % 40 == 20: res.append(i*val)
    if (i-1) % 40 in [val-1, val, val+1]: res.append("#")
    else: res.append('.')

# print(sum(res))
p = [res[i:i+40] for i in range(0, len(res), 40)]
for z in p:
    print(''.join(z))
file.close()