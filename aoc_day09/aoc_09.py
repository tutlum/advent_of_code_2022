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

data2="""R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20"""

vis = False

with open("data.txt", "r") as f:
    data=f.read()

data=[d.split(" ") for d in data.split("\n") if d!=""]

def dist(x,y):
    return max(abs(x-y))

def visualizepath(path):
    ws = Tk()
    ws.title('PythonGuides')
    ws.geometry('500x500')
    ws.config(bg='#345')
    scale=2
    minix=min([x[0] for x in path])
    width=scale*(max([x[0]-minix for x in path])+1)
    miniy=min([x[1] for x in path])
    height=scale*(max([x[1]-miniy for x in path])+1)
    canvas = Canvas(
        ws,
        height=height,
        width=width,
        bg="#fff"
        )
        
    canvas.pack()
    for x in path:
        canvas.create_rectangle(
            scale*(x[0]-minix), height-(scale*(x[1]-miniy)), scale*(x[0]-minix)+scale, height-(scale*(x[1]-miniy)+scale),
            outline="#fb0",
            fill="#fb0")
    ws.mainloop()


def first(data):
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
    visualizepath(singlehistory)
    

def second(data):
    rope=[np.array((0,0)) for i in range(10)]
    h=np.array((0,0))
    t=np.array((0,0))

    singlehistory=set()
    singlehistory.add(tuple(rope[9]))

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
            rope[0]=rope[0]+dr
            for r in range(9):
                if (max(abs(rope[r]-rope[r+1])) > 1):
                    rope[r+1]=rope[r+1]+np.array([int(i/abs(i)) if i!=0 else 0 for i in (rope[r]-rope[r+1])])
            tt=tuple(rope[9])
            singlehistory.add(tt)
    print(len(singlehistory))
        #print(singlehistory)
    visualizepath(singlehistory)
    
second(data)#[d.split(" ") for d in data2.split("\n") if d!=""])
