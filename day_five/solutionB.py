from typing import List

# opne the input file and convert its lines into a List[str]
file = open("input.txt")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

# will read a string of numbers and return a list with them
def strToList(s: str) -> List[int]:
    nums = s.split(" ")
    res = []
    for i in range(0, len(nums), 2):
        res.append([int(nums[i]), int(nums[i+1]) + int(nums[i]) - 1])
    return res

## In this approach, we will work on the intervals themselves. We will split them when neccessary and 
# convert the pieces, where possible. Merging requires sorting, and merging is required to have as few 
# intervals as possible
intervals = sorted(strToList(lines[0].split(": ")[1]))

conversionSets = [[]]
mapTo = [{}]

i, convSetCnt = 3, 0
while i < len(lines):
    if lines[i] == "":                          # moving to the next converter set
        conversionSets[convSetCnt].sort()
        conversionSets.append([])    # adding an empty converter set 
        mapTo.append({})
        convSetCnt+=1
        i+=2
        continue
    nums = lines[i].split(" ")
    newInterval = [int(nums[1]), int(nums[1]) + int(nums[2]) - 1]
    conversionSets[convSetCnt].append(newInterval)
    mapTo[convSetCnt][(newInterval[0], newInterval[1])] = int(nums[0])-int(nums[1])
    i+=1
conversionSets[convSetCnt].sort()

# merges all intervals in the list and returns the result as a new List
# sorting is done in the method
def merged(ints: List[List[int]]) -> List[List[int]]:
    res = []
    ints.sort()
    curInt = ints[0]
    for interval in ints:
        if curInt[1] >= interval[0]:
            curInt[1] = max(curInt[1], interval[1])
        else:
            res.append(curInt)
            curInt = interval
    res.append(curInt)
    return res
    
def isValid(interval: List[int]) -> bool:
    return len(interval) == 2 and interval[1] >= interval[0]

# finds the given interval in a subinterval and returns the new List, with the interval converted
# merging is done at the end
def converted(intsToFind: List[List[int]], ints: List[List[int]], step) -> List[List[int]]:
    res = []
    for intToFind in intsToFind:
        copyints = ints.copy()
        while len(copyints) > 0:
            int = ints.pop(0)
            copyints.pop(0)
            # the two intervals don't intersect
            if int[0] > intToFind[1] or int[1] < intToFind[0]:
                # print("skip")
                ints.append(int)
                continue
                
            # the interval is completely included
            elif (intToFind[0] <= int[1] and intToFind[0] >= int[0]) and (intToFind[1] <= int[1] and intToFind[1] >= int[0]):
                interval1 = [int[0], intToFind[0]-1]
                if isValid(interval1):
                    ints.append(interval1)
                addition = mapTo[step].get((intToFind[0], intToFind[1]), [])          
                interval2 = [intToFind[0]+addition, intToFind[1]+addition]  
                if isValid(interval2):
                    res.append(interval2)
                interval3 = [intToFind[1]+1, int[1]]
                if isValid(interval3):
                    ints.append(interval3)
            
            # the start of the interval is included only
            elif intToFind[0] <= int[1] and intToFind[0] >= int[0]:
                interval1 = [int[0], intToFind[0]-1]
                if isValid(interval1):
                    ints.append(interval1)
                addition = mapTo[step].get((intToFind[0], intToFind[1]), [])
                interval2 = [intToFind[0]+addition, int[1]+addition]
                if isValid(interval2):
                    res.append(interval2)
                    
            # the end of the interval is included only
            elif intToFind[1] <= int[1] and intToFind[1] >= int[0]:
                addition = mapTo[step].get((intToFind[0], intToFind[1]), [])
                interval1 = [int[0]+addition, intToFind[1]+addition]
                if isValid(interval1):
                    res.append(interval1)
                interval2 = [intToFind[1]+1, int[1]]
                if isValid(interval2):
                    ints.append(interval2)
            
            elif intToFind[1] >= int[1] and intToFind[0] <= int[0]:
                addition = mapTo[step].get((intToFind[0], intToFind[1]), [])
                interval1 = [int[0]+addition, int[1]+addition]            
                if isValid(interval1):
                    res.append(interval1)
        ints.sort()
    res.extend(ints)
    return merged(res)

for step in range(0, 7):
    intervals = converted(conversionSets[step], intervals, step)
intervals.sort()
print(intervals[0][0])

