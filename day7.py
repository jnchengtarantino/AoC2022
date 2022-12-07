import numpy as np
from collections import Counter, defaultdict
from functools import reduce 
from itertools import accumulate
# file = open("testinput.txt")
file = open("day7input.txt")

dirs = defaultdict(int)

lines = file.readlines()
for line in lines:
    match line.strip().split(" "):
        case '$', 'cd', '/' : curr = ['/']
        case '$', 'cd', '..' : curr.pop()
        case '$', 'cd', x : curr.append(x+'/')
        case '$', 'ls' : pass
        case 'dir', _ : pass
        case size, _:
            for path in accumulate(curr):
                dirs[path] += int(size)

used = dirs["/"]
total = 70000000
needed = 30000000

print(sum([size for size in dirs.values() if size <= 100000]))                      # part 1
print(min([size for size in dirs.values() if size >= (needed - (total - used))]))   # part 2
file.close()