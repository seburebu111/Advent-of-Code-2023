file = open("input.txt")
input = file.readlines()
for i in range(len(input)):
    input[i] = input[i][:-1]    # removing the \n

mat = [[-1] * len(input[0]) for _ in range(len(input))]

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

maxx = 0
queue = []
queue.append(findStart())
mat[queue[0][0]][queue[0][1]] = 0
while len(queue) != 0:
    i, j = queue[0][0], queue[0][1]
    queue.pop(0)[1]
    if isValid(i-1, j) and input[i][j] in "JL|S" and input[i-1][j] in "F7|" and mat[i-1][j] == -1:    # upper pipe
        queue.append((i-1, j))
        mat[i-1][j] = mat[i][j] + 1
        maxx = max(maxx, mat[i-1][j])
    if isValid(i+1, j) and input[i][j] in "F7|S" and input[i+1][j] in "LJ|" and mat[i+1][j] == -1:    # bottom pipe
        queue.append((i+1, j))
        mat[i+1][j] = mat[i][j] + 1
        maxx = max(maxx, mat[i+1][j])
    if isValid(i, j-1) and input[i][j] in "7J-S" and input[i][j-1] in "FL-" and mat[i][j-1] == -1:    # left pipe
        queue.append((i, j-1))
        mat[i][j-1] = mat[i][j] + 1
        maxx = max(maxx, mat[i][j-1])
    if isValid(i, j+1) and input[i][j] in "FL-S" and input[i][j+1] in "7J-" and mat[i][j+1] == -1:    # right pipe
        queue.append((i, j+1))
        mat[i][j+1] = mat[i][j] + 1
        maxx = max(maxx, mat[i][j+1])
    # print(mat)
print(maxx)
    
    