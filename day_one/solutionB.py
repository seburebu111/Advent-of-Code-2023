file = open("input.txt")
lines = file.readlines()    

def isDigit(line: str, i: int) -> bool:
    map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0} 
    if line[i] in "0123456789":
        return True
    if i+3 < len(line) and map.get(line[i:i+3], -1) != -1:
        return True
    if i+4 < len(line) and map.get(line[i:i+4], -1) != -1:
        return True
    if i+5 < len(line) and map.get(line[i:i+5], -1) != -1:
        return True
    return False

def getDigit(line: str, i: int) -> int:
    map = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "zero": 0} 
    if line[i] in "0123456789":
        return ord(line[i]) - ord("0")
    if i+3 < len(line) and map.get(line[i:i+3], -1) != -1:
        return map[line[i:i+3]]
    if i+4 < len(line) and map.get(line[i:i+4], -1) != -1:
        return map[line[i:i+4]]
    if i+5 < len(line) and map.get(line[i:i+5], -1) != -1:
        return map[line[i:i+5]]
    return -1

sum = 0
for line in lines:
    l, r = 0, len(line)-2   # without the last character ('\n')
    while not isDigit(line, l):
        l+=1
    while not isDigit(line, r):
        r-=1
    
    sum += getDigit(line, l)*10+getDigit(line, r)
    
print(sum)
