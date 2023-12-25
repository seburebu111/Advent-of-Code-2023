mapLeft = {}
mapRight = {}

file = open("input.txt")
lines = file.readlines()

moves = lines[0][:-1]

for line in lines[2:]:
    curr = line[:3]
    left = line[7:10]
    right = line[12:-2]  
    mapLeft[curr] = left
    mapRight[curr] = right

moveCnt = 0
curr = "AAA"
while curr != "ZZZ":
    for move in moves:
        # print(curr, "move: ", move, "moveCnt: ", moveCnt)
        if move == "L":
            curr = mapLeft[curr]
        else:
            curr = mapRight[curr]
        moveCnt += 1
print(moveCnt)
