import numpy as np
from collections import Counter
import itertools
# file = open("testinput.txt")
file = open("day2input.txt")

score = 0
theyDict = {
    'A':1,
    'B':2,
    'C':3
}

meDict = {
    'X':0,
    'Y':3,
    'Z':6
}

lines = file.readlines()
for line in lines:
    they, me = line.strip().split(" ")
    they = theyDict[they]
    me = meDict[me]
    print(me)
    score += me
    theyMod = they -1
    if me == 0: theyMod-=1
    elif me == 6: theyMod+=1
    theyMod = theyMod%3 + 1
    score+=theyMod
    print(theyMod)
    print(score)
    print()

print(score)   

file.close()