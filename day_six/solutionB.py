import math
from typing import List

# opne the input file and convert its lines into a List[str]
file = open("input.txt")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

# will read a string of numbers and return a list with them
def kernelStrToInt(s: str) -> List[int]:
    nums = s.split(" ")
    res = ""
    for num in nums:
        if num == "":
            continue
        res += num
    return int(res)

t = kernelStrToInt(lines[0].split(": ")[1])
d = kernelStrToInt(lines[1].split(": ")[1])

# the points of in which the record was made is found by the formula
# x1,2 = (t +/- sqrt(t^2-4d))/2

x1 = (t - math.sqrt(t**2 - 4*d))/2
x2 = (t + math.sqrt(t**2 - 4*d))/2

x1, x2 = int(x1), int(x2+0.99999) # x1 and x2 will be the edge values, the ones which won't beat the record
# the integers in (x1, x2) are the values which would beat the record
# adding 0.99999, will increase every number to the next integer, but the ones who already are integers

res = x2-x1-1
    
print(res)
    
    
