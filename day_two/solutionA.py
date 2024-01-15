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

#checks whether a game can be possible using only 12 red cubes, 13 green cubes, and 14 blue cubes
def isGameValid(game: str) -> bool:
    rounds = game.split(": ")[1].split("; ")
    for round in rounds:
        colors = getColors(round)
        if colors[0] > 14 or colors[1] > 12 or colors[2] > 13:
            return False
    return True

res = 0
for game in games:
    gameNo = strToInt(game.split(": ")[0][5:])
    if isGameValid(game):
        res += gameNo
print(res)
    
        
