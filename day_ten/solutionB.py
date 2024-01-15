file = open("input.txt")
input = file.readlines()
for i in range(len(input)):
    input[i] = input[i][:-1]    # removing the \n

mat = [[False] * len(input[0]) for _ in range(len(input))]

def findStart() -> (int, int):
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == "S":
                return (i, j)
            
def isValid(i: int, j: int) -> bool:
    if i < 0 or i >= len(input):
        return False
    if j < 0 or j >= len(input[0]):
        return False
    return True

# find all important pipes, and put 1 in mat
queue = []
queue.append(findStart())
mat[queue[0][0]][queue[0][1]] = True
while len(queue) != 0:
    i, j = queue[0][0], queue[0][1]
    queue.pop(0)[1]
    if isValid(i-1, j) and input[i][j] in "JL|S" and input[i-1][j] in "F7|" and mat[i-1][j] == False:    # upper pipe
        queue.append((i-1, j))
        mat[i-1][j] = True
    if isValid(i+1, j) and input[i][j] in "F7|S" and input[i+1][j] in "LJ|" and mat[i+1][j] == False:    # bottom pipe
        queue.append((i+1, j))
        mat[i+1][j] = True
    if isValid(i, j-1) and input[i][j] in "7J-S" and input[i][j-1] in "FL-" and mat[i][j-1] == False:    # left pipe
        queue.append((i, j-1))
        mat[i][j-1] = True
    if isValid(i, j+1) and input[i][j] in "FL-S" and input[i][j+1] in "7J-" and mat[i][j+1] == False:    # right pipe
        queue.append((i, j+1))
        mat[i][j+1] = True
print(mat)

def findStartSymbol(start: (int, int)) -> str:
    # find suitable symbol for start
    if isValid(start[0] + 1, start[1]) and input[start[0] + 1][start[1] - 1] != "." and isValid(start[0] - 1, start[1]) and input[start[0] - 1][start[1]] != ".":
        return "|"
        
    elif isValid(start[0], start[1] + 1) and input[start[0]][start[1] + 1] != "." and isValid(start[0], start[1] - 1) and input[start[0]][start[1] - 1] != ".":
        return "-"
        
    elif isValid(start[0] - 1, start[1]) and input[start[0] - 1][start[1]] != "." and isValid(start[0], start[1] + 1) and input[start[0]][start[1] + 1] != ".":
        return "L"
        
    elif isValid(start[0] + 1, start[1]) and input[start[0] + 1][start[1]] != "." and isValid(start[0], start[1] + 1) and input[start[0]][start[1] + 1] != ".":
        return "F"
        
    elif isValid(start[0] + 1, start[1]) and input[start[0] + 1][start[1]] != "." and isValid(start[0], start[1] - 1) and input[start[0]][start[1] - 1] != ".":
        return "7"
        
    elif isValid(start[0] + 1, start[1]) and input[start[0] + 1][start[1]] != "." and isValid(start[0], start[1] - 1) and input[start[0]][start[1] - 1] != ".":
        return "J"

input2 = []
# mark all other pipes with '.'
for i in range(len(input)):
    input2.append([])
    for j in range(len(input[i])):
        if mat[i][j] == False:
            input2[i].append(".")
        else:
            if input[i][j] == "S":
                input2[i].append(findStartSymbol((i, j)))  
            else:
                input2[i].append(input[i][j])          
print(input2)
