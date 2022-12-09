import numpy as np
from collections import Counter, defaultdict
from functools import reduce
from itertools import accumulate
# file = open("testinput.txt")
file = open("day9input.txt")

k =[[0,0] for _ in range(10)]
visited = {(0,0)}

def step(dir, n):
    for _ in range(n):
        match dir:
            case 'R': k[0][0] += 1
            case 'L': k[0][0] -= 1
            case 'U': k[0][1] += 1
            case 'D': k[0][1] -= 1
        
        for i in range(1,10):
            v = [(hi - ti) for hi, ti in zip(k[i-1],k[i])]
            # print("V: " + str(v))

            if (v[0] > 1):
                k[i][0] += 1
                if (v[1] > 0):
                    k[i][1] += 1
                elif (v[1] < 0):
                    k[i][1] -= 1

            elif (v[0] < -1):
                k[i][0] -= 1
                if (v[1] > 0):
                    k[i][1] += 1
                elif (v[1] < 0):
                    k[i][1] -= 1

            elif (v[1] > 1):
                k[i][1] += 1
                if (v[0] > 0):
                    k[i][0] += 1
                elif (v[0] < 0):
                    k[i][0] -= 1

            elif (v[1] < -1):
                k[i][1] -= 1
                if (v[0] > 0):
                    k[i][0] += 1
                elif (v[0] < 0):
                    k[i][0] -= 1

        visited.add((k[-1][0], k[-1][1]))
       

lines = file.readlines()
for line in lines:
    dir, n = line.strip().split(" ")
    # print(line.strip())
    step(dir, int(n))

print(len(visited))
file.close()