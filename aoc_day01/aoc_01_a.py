import numpy as np

data=""
with open("data.txt", "r") as f:
	data = f.read()
	
elves=data.split("\n\n")
calories=[sum([int(cs) for cs in e.split("\n") if cs!=""]) for e in elves]

arr=np.array(calories)
arr.sort()
print(sum(arr[-3:]))
print(calories)
