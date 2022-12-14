import numpy as np
from tkinter import *

vis = False

with open("data.txt", "r") as f:
    data=f.read()

data=[d.split(" ") for d in data.split("\n") if d!=""]

cycles=[0]
registers=[1]
screen=[" " for i in range(240)]

def evalCycl(cycles, registers):
    cycles[0]=cycles[0]+1
    if ((cycles[0]-1)%40-1 <= registers[0] <= (cycles[0]-1)%40+1):
        screen[cycles[0]-1]="#"
    if ((cycles[0]-20)%40==0):
        print(registers[0], cycles[0], registers[0]*cycles[0])
        return registers[0]*cycles[0]
    else:
        return 0

strength=0
for d in data:
    if (d[0]=="noop"):
        strength+=evalCycl(cycles, registers)
    elif (d[0]=="addx"):
        strength+=evalCycl(cycles, registers)
        strength+=evalCycl(cycles, registers)
        registers[0]=registers[0]+int(d[1])
    
print(strength)

for i in range(int(240/40)):
    for j in range(40):
        print(screen[i*40+j], end="")
    print("\n", end="")
