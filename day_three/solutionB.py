file = open("input.txt")
lines = file.readlines()
n, m = len(lines), len(lines[0])-1
for i in range(n):
    lines[i] = lines[i].replace("\n", "")
vis = [[False] * m for _ in range(n)]

def charToInt(s: str) -> int:
    return ord(s) - ord("0")

def strToInt(s: str) -> int:
    res = 0
    for c in s:
        res = res*10+charToInt(c)
    return res

def getNum(line: str, i: int, j: int) -> int:
    l, r = j, j
    while l >= 0 and line[i][l] in "1234567890":
        l-=1
    l+=1
    while r < m and line[i][r] in "1234567890":
        r+=1
    for index in range(l, r):
        vis[i][index] = True
    return strToInt(line[i][l:r])

def isValidMove(newi: int, newj: int) -> bool:
    if newi < 0 or newj < 0:
        return False
    if newi >= n or newj >= m:
        return False
    return True

# # any number adjacent to a symbol, even diagonally, is a "part number". "." is not a symbol
# def isPartNum(s: str, i: int, j: int) -> bool:
#     for move in moves:
#         if isValidMove(i+move[0], j+move[1]) and lines[i+move[0]][j+move[1]] not in ".1234567890":
#             sum += getNum(lines[i+move[0]], j+move[1])


sum = 0
moves = [[-1, -1], [-1, 0], [-1, 1], [1, -1], [1, 0], [1, 1], [0, -1], [0, 1]]
for i in range(n):
    for j in range(m):
        if lines[i][j] == "*":
            cnt, prod = 0, 1
            for move in moves:
                if isValidMove(i+move[0], j+move[1]) and lines[i+move[0]][j+move[1]].isnumeric() and vis[i+move[0]][j+move[1]] == False:
                    prod *= getNum(lines, i+move[0], j+move[1])
                    cnt += 1
            if cnt == 2:
                sum += prod
print(sum)
