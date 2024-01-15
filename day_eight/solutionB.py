mapLeft = {}
mapRight = {}

file = open("input.txt")
lines = file.readlines()

moves = lines[0][:-1]
starts = []

for line in lines[2:]:
    curr = line[:3]
    if curr[-1] == "A":
        starts.append(curr)
    left = line[7:10]
    right = line[12:-2]  
    mapLeft[curr] = left
    mapRight[curr] = right

def getMoveCnt(start: str):
    moveCnt = 0
    curr = start
    while curr[-1] != "Z":
        for move in moves:
            # print(curr, "move: ", move, "moveCnt: ", moveCnt)
            if move == "L":
                curr = mapLeft[curr]
            else:
                curr = mapRight[curr]
        moveCnt += 1
    return moveCnt

def gcd(a: int, b: int) -> int:
    gcd = 1
    d = 1
    while d <= min(a, b):
        if a%d == 0 and b%d == 0:
            gcd = d
        d+=1
    return gcd

def scm(a: int, b: int) -> int:
    return a*b // gcd(a, b)

# the numebr of move sets for each starting position
nums = []
for start in starts:
    nums.append(getMoveCnt(start))

# find the smallest common multiple of all the starting positions
curr = nums[0]
for num in nums:
    curr = scm(num, curr)
print(curr * len(moves))

