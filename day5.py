import numpy as np
from collections import Counter
from functools import reduce
# file = open("testinput.txt")
file = open("day5input.txt") 

data = None
instructions = False

lines = file.readlines()
for line in lines:
    if data == None:
        data = [[] for i in range((len(line)//4))]

    if not instructions:
        if line.strip() == '':
            instructions = True
        else:
            if '[' in line:
                crates = [c for c in line[1::4]]

                for i in range(len(crates)):
                    if crates[i].strip() != '':
                        data[i].insert(0, crates[i])

    else:
        num, start, end = [int(x) for x in line.split()[1::2]]

        # part 1
        # for i in range(num):
        #     data[end - 1].append(data[start - 1].pop())

        data[end-1] += data[start-1][-num:]
        data[start-1] = data[start-1][0:-num]

print(reduce(lambda x,y: x+y.pop(), data, ''))

file.close()