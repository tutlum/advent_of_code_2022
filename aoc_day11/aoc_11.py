from functools import reduce

data="""Monkey 0:
  Starting items: 79, 98
  Operation: new = old * 19
  Test: divisible by 23
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 54, 65, 75, 74
  Operation: new = old + 6
  Test: divisible by 19
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 2:
  Starting items: 79, 60, 97
  Operation: new = old * old
  Test: divisible by 13
    If true: throw to monkey 1
    If false: throw to monkey 3

Monkey 3:
  Starting items: 74
  Operation: new = old + 3
  Test: divisible by 17
    If true: throw to monkey 0
    If false: throw to monkey 1"""

# ~ with open("data.txt", "r") as f:
    # ~ data=f.read()
    
data="""Monkey 0:
  Starting items: 76, 88, 96, 97, 58, 61, 67
  Operation: new = old * 19
  Test: divisible by 3
    If true: throw to monkey 2
    If false: throw to monkey 3

Monkey 1:
  Starting items: 93, 71, 79, 83, 69, 70, 94, 98
  Operation: new = old + 8
  Test: divisible by 11
    If true: throw to monkey 5
    If false: throw to monkey 6

Monkey 2:
  Starting items: 50, 74, 67, 92, 61, 76
  Operation: new = old * 13
  Test: divisible by 19
    If true: throw to monkey 3
    If false: throw to monkey 1

Monkey 3:
  Starting items: 76, 92
  Operation: new = old + 6
  Test: divisible by 5
    If true: throw to monkey 1
    If false: throw to monkey 6

Monkey 4:
  Starting items: 74, 94, 55, 87, 62
  Operation: new = old + 5
  Test: divisible by 2
    If true: throw to monkey 2
    If false: throw to monkey 0

Monkey 5:
  Starting items: 59, 62, 53, 62
  Operation: new = old * old
  Test: divisible by 7
    If true: throw to monkey 4
    If false: throw to monkey 7

Monkey 6:
  Starting items: 62
  Operation: new = old + 2
  Test: divisible by 17
    If true: throw to monkey 5
    If false: throw to monkey 7

Monkey 7:
  Starting items: 85, 54, 53
  Operation: new = old + 3
  Test: divisible by 13
    If true: throw to monkey 4
    If false: throw to monkey 0"""
    

    
def getValue(old, number):
    if (number=="old"):
        return old
    else:
        return int(number)
    
def calcWorry(i, op):
    if (op[0]=="+"):
        return i+getValue(i, op[1])
    elif (op[0]=="-"):
        return i-getValue(i, op[1])
    elif (op[0]=="*"):
        return i*getValue(i, op[1])
    elif (op[0]=="/"):
        return i/getValue(i, op[1])

data=[[dd.split(":")[1].strip() for dd in d.split("\n")[1:]] for d in data.split("\n\n") if d!=""]
#print(data)

for d in data:
    d[0]=[int(x.strip()) for x in d[0].split(",")]
    sp=d[1].split(" ")
    d[1]=[sp[-2], sp[-1]]
    for i in range(2,5):
        d[i]=int(d[i].split(" ")[-1])
    d.append(0)

def track_round(monkeys, rest):
    for mi in range(len(monkeys)):
        m=monkeys[mi]
        for i in range(len(m[0])):
            wV=int(calcWorry(m[0].pop(0), m[1])%rest)
            m[5]+=1
            if (wV%m[2]==0):
                #print("throw", wV, "to", m[3])
                monkeys[m[3]][0].append(wV)
            else:
                #print("throw", wV, "to", m[4])
                monkeys[m[4]][0].append(wV)
                
rules=reduce((lambda x, y: x * y), [m[2] for m in data])
                
for i in range(10000):
    print(i)
    track_round(data, rules)
    if (i%10==0):
        print(data)
    
busy=[m[5] for m in data]
busy.sort()
print(busy[-1]*busy[-2])

print(data)
