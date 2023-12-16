from typing import List

file = open("input.txt")
games = file.readlines()

def charToInt(s: str) -> int:
    return ord(s) - ord("0")

def strToInt(s: str) -> int:
    res = 0
    for c in s:
        res = res*10+charToInt(c)
    return res

# returns a list of numbers representing the number of cubes of each color:
# [blue, red, green]
def getColors(round: str) -> List[int]:
    b, r, g = 0, 0, 0
    for draw in round.split(", "):
        color = draw.split()[1]
        if color == "blue":
            b = strToInt(draw.split()[0])
        if color == "green":
            g = strToInt(draw.split()[0])
        if color == "red":
            r = strToInt(draw.split()[0])
    return [b, r, g]

# the power of a set of cubes is equal to the numbers of red, green, and blue cubes multiplied together.
def getPower(game: str) -> int:
    rounds = game.split(": ")[1].split("; ")
    maxb, maxg, maxr = 0, 0, 0
    for round in rounds:
        colors = getColors(round)
        maxb = max(maxb, colors[0])
        maxr = max(maxr, colors[1])
        maxg = max(maxg, colors[2])
    return maxb*maxg*maxr

res = 0
for game in games:
    res += getPower(game)
print(res)
    
        
