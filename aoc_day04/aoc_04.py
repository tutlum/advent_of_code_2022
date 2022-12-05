import numpy as np

data="""
2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def inclusion(a,b,c,d):
    return ((int(a)<=int(c) and int(b)>=int(d)) or (int(a)>=int(c) and int(b)<=int(d)))
    
def overlap(a,b,c,d):
    return ((int(b)>=int(c) and int(b)<=int(d)) or (int(a)>=int(c) and int(a)<=int(d)) or (int(a)<=int(c) and int(b)>=int(d)))

with open("data.txt", "r") as f:
    data=f.read()

assignments = [d.split(",") for d in data.split("\n") if d!=""]

inclusions=0
overlaps=0
for ass in assignments:
    (a,b)=ass[0].split("-")
    (c,d)=ass[1].split("-")
    if inclusion(a,b,c,d):
        inclusions=inclusions+1
    if overlap(a,b,c,d):
        overlaps=overlaps+1

print(inclusions)
print(overlaps)
        
