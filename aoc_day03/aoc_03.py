import numpy as np
from functools import reduce

data="""
vJrwpWtwJgWrhcsFMMfFFhFp
jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
PmmdzqPrVvPwwTWBwg
wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
ttgJtRGJQctTZtZT
CrZsJsPPZsGzwwsLwLmpwMDw
"""

with open("data.txt", "r") as f:
    data=f.read()

backpacks = [np.array([(ord(i)-96) if ord(i)>96 else (ord(i)-38) for i in d]) for d in data.split("\n") if d!=""]

unique_items = [np.intersect1d(a[0:int(a.size/2)],a[int(a.size/2):])[0] for a in backpacks]

print( sum(unique_items))

badges = [reduce(np.intersect1d, (backpacks[i],backpacks[i+1],backpacks[i+2]))[0] for i in range(0,len(backpacks),3)]

print( sum( badges ) )
