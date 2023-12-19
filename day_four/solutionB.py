from typing import List

file = open("input.txt")
lines = file.readlines()
# print(lines)
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")
    # print(lines[i])

def charToInt(s: str) -> int:
    return ord(s) - ord("0")

def strToInt(s: str) -> int:
    res = 0
    for c in s:
        res = res*10+charToInt(c)
    return res

def strToList(s: str) -> List[int]:
    sNums = s.split(" ")
    res = []
    for snum in sNums:
        if snum == "":
            continue
        res.append(strToInt(snum))
    return res

def cardValue(s: str) -> int:
    s = s.split(": ")[1]
    winning = {}
    for num in strToList(s.split(" | ")[0]):
        winning[num] = True
    # print(winning)
    value = 0
    for num in strToList(s.split(" | ")[1]):
        if winning.get(num, False) == True:
            # print("***")
            # print(num)
            value += 1
    return value

ponder = [1] * len(lines)
res = 0 
for i in range(len(lines)):
    # print(ponder)
    card = lines[i]
    value = cardValue(card)
    # print(card, value)
    res += ponder[i]
    if value > 0:
        for j in range(i+1, min(len(lines), i+value+1)):
            ponder[j] += ponder[i]
print(res)
        
    
        