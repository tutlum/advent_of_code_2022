import numpy as np
import re

data="""nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg"""

with open("data.txt", "r") as f:
    data=f.read()
def detect(distinct):
    for i in range(distinct,len(data)):
        if (len(set(data[i-distinct+1:i+1]))==distinct):
            print(set(data[i-distinct+1:i+1]),i+1)
            break

detect(14)
