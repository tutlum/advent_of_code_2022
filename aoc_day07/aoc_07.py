import numpy as np
import re

data="""$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

with open("data.txt", "r") as f:
    data=f.read()

data=[d for d in data.split("\n") if d!=""]

def getbranch(tree, dirs):
    if (len(dirs)==0):
        return tree
    else:
        return getbranch(tree[dirs[0]],dirs[1:])
        
def printtree(tree, pos):
    ret=""
    if (isinstance(tree, str)):
        ret= tree
    else:
        ret="\n"
        ret=ret + "\n".join([((pos*"  ") + b + ": " + printtree(tree[b], pos+1)) for b in tree])
    return ret
    
def calcdirsize(tree, sizelist):
    s=0
    for e in tree:
        if (isinstance(tree[e], str)):
            s=s+int(tree[e])
        else:
            s=s+calcdirsize(tree[e],sizelist)
    sizelist.append(s)
    return s

tree={}
cposition=[]

for d in data:
    c=d.split(" ")
    if (c[0]=="$"):
        if (c[1]=="cd"):
            if (c[2]=="/"):
                cposition=[]
            elif (c[2]==".."):
                cposition.pop()
            else:
                branch=getbranch(tree, cposition)
                cposition.append(c[2])
                if (c[2] not in branch):
                    branch[c[2]]={}
    else:
        branch=getbranch(tree, cposition)
        if (c[1] not in branch):
            if (c[0]=="dir"):
                branch[c[1]]={}
            else:
                branch[c[1]]=c[0]
                
print("/:" + printtree(tree, 1))

sizelist=[]
all_used= calcdirsize(tree, sizelist)
print("sum of all small: ", sum([e for e in sizelist if e<100000]))

available=70000000
needed=30000000
min_to_free=needed-(available-all_used)
# print(all_used)
# print(min_to_free)

print("size of freeing dir: ", min([e for e in sizelist if e>min_to_free]))

