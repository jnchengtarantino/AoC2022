import numpy as np
from collections import Counter
import itertools
# file = open("testinput.txt")
file = open("day4input.txt")

count = 0

lines = file.readlines()
for line in lines:
    r1, r2 = line.strip().split(',')
    l1, u1 = r1.split('-')
    l2, u2 = r2.split('-')

    elf1 = set(range(int(l1), int(u1) + 1))
    elf2 = set(range(int(l2), int(u2) + 1))

    # combined = elf1.union(elf2)
    # if combined == elf1 or combined == elf2: count += 1

    inter = elf1.intersection(elf2)
    if set() != inter: count += 1

print(count)
        
file.close()