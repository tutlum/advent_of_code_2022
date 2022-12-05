import numpy as np

data="""
A Y
B X
C Z
"""
with open("data.txt", "r") as f:
	data = f.read() 
	
def win(move, answer):
	if ((move=="A" and answer=="Y") or (move=="B" and answer=="Z") or (move=="C" and answer=="X")):
		return 6
	elif (ord(move)==ord(answer)-23):
		return 3
	else:
		return 0
def movescore(move, answer):
	if (answer=="Z"):
		if (move=="A"):
			return 2
		elif (move=="B"):
			return 3
		else: return 1
	elif (answer=="Y"):
		return ord(move)-64
	else:
		if (move=="A"):
			return 3
		elif (move=="B"):
			return 1
		else: return 2
def win2(answer):
	if (answer=="X"):
		return 0
	elif (answer=="Y"):
		return 3
	else:
		return 6

def score(move, answer):
	return ord(answer)-87+win(move, answer)
def score2(move, answer):
	return movescore(move, answer)+win2(answer)
			
moves=data.split("\n")
moves=[m.split(" ") for m in moves if " " in m]


scores=[score(*m) for m in moves]
scores2=[score2(*m) for m in moves]

print(sum(scores))
print(sum(scores2))

	
