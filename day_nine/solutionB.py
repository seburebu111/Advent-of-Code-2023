from typing import List

file = open("input.txt")
lines = file.readlines()

for i in range(len(lines)):
    lines[i] = lines[i][:-1]

def strToList(s: str) -> List[int]:
    res = []
    nums = s.split(" ")
    for num in nums:
        res.append(int(num))
    return res

def notNull(l: List[int]) -> bool:
    for num in l:
        if num != 0:
            return True
    return False

sum = 0
for line in lines:
    table = [strToList(line)]
    i = 0
    # create a table with every iteration of the difference between two the numbers positioned the row above
    while notNull(table[i]):
        table.append([table[i][j+1] - table[i][j] for j in range(len(table[i])-1)])
        i+=1
    # add a 0 to the start of the last row instead of the end
    table[-1].insert(0, 0)
    
    # go up, adding inserting at the beginning an element to each iteration of the table
    for i in range(len(table)-2, -1, -1):
        table[i].insert(0, table[i][0] - table[i+1][0])

    # the newly added element is at the start of the first line
    sum += table[0][0]
print(sum)
