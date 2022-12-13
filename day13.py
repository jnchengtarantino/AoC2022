import numpy as np
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
from math import lcm
# file = open("testinput.txt")
file = open("day13input.txt")

# ctr = 1
# sum = 0
buffer = []

def compare(l, r):
    if isinstance(l, int) and isinstance(r, list):
        l = [l]
    if isinstance(l, list) and isinstance(r, int):
        r = [r]
    
    if isinstance(l, int) and isinstance(r, int):
        if l < r:
            return True
        elif l > r:
            return False
        else:
            return None
    
    if isinstance(l, list) and isinstance(r, list):
        for i in range(min(len(l), len(r))):
            ret = compare(l[i], r[i])
            if ret is None:
                continue
            else:
                return ret
                
        else:
            if len(l) < len(r):
                return True
            elif len(l) > len(r):
                return False
            else:
                return None

    


lines = file.readlines()
lines.append('[[2]]')
lines.append('[[6]]')
for line in lines:
    if line.strip() == '': continue
    val = eval(line.strip())
    for i in range(len(buffer)):
        if compare(val, buffer[i]):
            buffer.insert(i, val)
            break
    else:
        buffer.append(val)

    # if line.strip() == '': buffer = []
    # else :
    #     buffer.append(eval(line.strip()))
    
    #     if len(buffer) == 2:
    #         if compare(buffer[0], buffer[1]): sum += ctr
    #         ctr += 1

print(buffer)
print( (buffer.index([[2]]) + 1) * (buffer.index([[6]]) + 1) )
file.close()