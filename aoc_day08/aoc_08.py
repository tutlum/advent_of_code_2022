import numpy as np
import re

data="""30373
25512
65332
33549
35390"""

vis = False

with open("data.txt", "r") as f:
    data=f.read()

data=[d for d in data.split("\n") if d!=""]

def isVisible(x,y,grid):
    somebigger=False
    for i in range(x+1,len(grid[0])):
        if (grid[y][i]>=grid[y][x]):
            somebigger=True
            break
    if (not somebigger):
        return True
    somebigger=False
    for i in range(0,x):
        if (grid[y][i]>=grid[y][x]):
            somebigger=True
            break
    if (not somebigger):
        return True
    somebigger=False
    for i in range(y+1,len(grid)):
        if (grid[i][x]>=grid[y][x]):
            somebigger=True
            break
    if (not somebigger):
        return True
    somebigger=False
    for i in range(0,y):
        if (grid[i][x]>=grid[y][x]):
            somebigger=True
            break
    if (not somebigger):
        return True
        
def scenicScore(x,y,grid):
    score1=0
    for i in range(x+1,len(grid[0])):
        score1+=1
        if (grid[y][i]>=grid[y][x]):
            break
    if (score1==0):
        return 0
    score2=0
    for i in range(x-1,-1,-1):
        score2+=1
        if (grid[y][i]>=grid[y][x]):
            break
    if (score2==0):
        return 0
    score3=0
    for i in range(y+1,len(grid)):
        score3+=1
        if (grid[i][x]>=grid[y][x]):
            break
    if (score3==0):
        return 0
    score4=0
    for i in range(y-1,-1,-1):
        score4+=1
        if (grid[i][x]>=grid[y][x]):
            break
    if (score4==0):
        return 0
    return score1*score2*score3*score4

if (vis):
    visGrid=[[0 for i in range(len(data[0]))] for j in range(len(data))]
    for x in range(len(data[0])):
        visGrid[0][x]=1
        visGrid[len(data)-1][x]=1
    for y in range(1,len(data)-1):
        visGrid[y][0]=1
        visGrid[y][len(data[0])-1]=1

visible=len(data[0])*2+len(data)*2-4
for x in range(1,len(data[0])-1):
    for y in range(1,len(data)-1):
        if (isVisible(x,y,data)):
            if (vis): visGrid[y][x]=1
            visible=visible+1
            

print("visible: ", visible)

visGrid=[[0 for i in range(len(data[0]))] for j in range(len(data))]
for x in range(1,len(data[0])-1):
    for y in range(1,len(data)-1):
        visGrid[y][x]=scenicScore(x,y,data)
if (vis):
    for i in visGrid:
        print(i)

#print("max view: ", max([max([scenicScore(x,y,data) for x in range(1,len(data[0])-1)]) for y in range(1,len(data)-1)]))
print("max view: ", max([max(visGrid[y]) for y in range(1,len(data)-1)]))
