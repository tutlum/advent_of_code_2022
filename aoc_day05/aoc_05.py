import numpy as np
import re

data="""    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

with open("data.txt", "r") as f:
    data=f.read()

(containers, rules) = data.split("\n\n")
containerrows=containers.split("\n")

stacks=[]

for stacknr in range(1,len(containerrows[1]),4):
    stack=[]
    for row in range(len(containerrows)-2,-1,-1):
        if (containerrows[row][stacknr]!=" "):
            stack.append(containerrows[row][stacknr])
    stacks.append(stack)

print(stacks)

rules=[r for r in rules.split("\n") if r!=""]

newV=True

for r in rules:
    result = re.search(r"move (\d*) from (\d*) to (\d*)", r)
    move = result.groups()
    for p in range(int(move[0]),0,-1):
        stacks[int(move[2])-1].append(stacks[int(move[1])-1].pop(-p if newV else -1))


print("".join([s[-1] for s in stacks]))
