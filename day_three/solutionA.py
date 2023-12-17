from typing import List

file = open("input.txt")
lines = file.readlines()
n, m = len(lines), len(lines[0])-1
for i in range(n):
    lines[i] = lines[i].replace("\n", "")

def charToInt(s: str) -> int:
    return ord(s) - ord("0")

def strToInt(s: str) -> int:
    res = 0
    for c in s:
        res = res*10+charToInt(c)
    return res

def getNum(line: str, i: int, j: int) -> List[int]:
    l, r = j, j
    while l >= 0 and line[i][l] in "1234567890":
        l-=1
    l+=1
    while r < m and line[i][r] in "1234567890":
        r+=1
    return [l, r-1, strToInt(line[i][l:r])]

def isValidMove(newi: int, newj: int) -> bool:
    if newi < 0 or newj < 0:
        return False
    if newi >= n or newj >= m:
        return False
    return True

# any number adjacent to a symbol, even diagonally, is a "part number". "." is not a symbol
def isPartNum(s: str, i: int, l: int, r: int) -> bool:
    for j in range(l, r+1):
        for move in moves:
            if isValidMove(i+move[0], j+move[1]) and lines[i+move[0]][j+move[1]] not in ".1234567890":
                return True


sum = 0
moves = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, -1], [0, 1]]
i = 0
while i < n:
    j = 0
    while j < m:
        if lines[i][j] in "0123456789":
            # we found a digit
            resGetNum = getNum(lines, i, j)
            if isPartNum(lines, i, resGetNum[0], resGetNum[1]):
                sum += resGetNum[2]
            j = resGetNum[1]
        j+=1
    i+=1
print(sum)
