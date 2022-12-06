import numpy as np
from collections import Counter
from functools import reduce
# file = open("testinput.txt")
file = open("day6input.txt")

lines = file.readlines()
for line in lines:
    buffer = [c for c in line[:14]]
    for i in range(14, len(line)):
        if len(set(buffer)) == 14:
            print(i)
            break
        else: 
            buffer.pop(0)
            buffer.append(line[i])

        
file.close()