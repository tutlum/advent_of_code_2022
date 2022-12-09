import numpy as np
from tkinter import *
data="""R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2"""

vis = False

with open("data.txt", "r") as f:
    data=f.read()

data=[d.split(" ") for d in data.split("\n") if d!=""]

def dist(x,y):
    return max(abs(x-y))

h=np.array((0,0))
t=np.array((0,0))

singlehistory=set()
singlehistory.add(tuple(t))

for d in data:
    dx,dy=0,0
    if (d[0]=="R"):
        dx=1
    elif (d[0]=="L"):
        dx=-1
    elif (d[0]=="U"):
        dy=1
    elif (d[0]=="D"):
        dy=-1
    dr=np.array([dx,dy])
    for i in range(int(d[1])):
        h=h+dr
        if (max(abs(h-t)) > 1):
            t=t+np.array([int(i/abs(i)) if i!=0 else 0 for i in (h-t)])
        tt=tuple(t)
        singlehistory.add(tt)
print(len(singlehistory))
#print(singlehistory)

def visualizepath(path):
    ws = Tk()
    ws.title('PythonGuides')
    ws.geometry('500x500')
    ws.config(bg='#345')
    scale=2
    minix=min([x[0] for x in singlehistory])
    width=scale*(max([x[0]-minix for x in singlehistory])+1)
    miniy=min([x[1] for x in singlehistory])
    height=scale*(max([x[1]-miniy for x in singlehistory])+1)
    canvas = Canvas(
        ws,
        height=height,
        width=width,
        bg="#fff"
        )
        
    canvas.pack()
    for x in singlehistory:
        canvas.create_rectangle(
            scale*(x[0]-minix), height-(scale*(x[1]-minix)), scale*(x[0]-minix)+scale, height-(scale*(x[1]-minix)+scale),
            outline="#fb0",
            fill="#fb0")
    ws.mainloop()
visualizepath(singlehistory)
