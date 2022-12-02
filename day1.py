import numpy as np
from collections import Counter
import itertools
# file = open("testinput.txt")
file = open("day1input.txt")

lines = file.readlines()
results = []
run = 0
for line in lines:
    if line.strip() == '':
        results.append(run)
        run = 0
    else :
        run += int(line.strip())

results.append(run)
run = 0
results.sort()

print(sum(results[-3:]))
        
file.close()