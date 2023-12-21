from typing import List

class Converter:
    # create a new converter, given the three numbers: 
    # the destination range start, the source range start, and the range length.
    def __init__(self, s: str):
        nums = s.split(" ")
        self.mapTo = int(nums[0])
        self.mapFrom = int(nums[1])
        self.length = int(nums[2])
    
    # check whether this converter is suitable for the given number
    def isInConverter(self, num: int) -> bool:
        return (num >= self.mapFrom and num < self.mapFrom + self.length)
    
    # converts the given number
    def convert(self, num: int) -> int:
        return num - (self.mapFrom - self.mapTo)
    
class ConverterSet:
    # initializes an empty ConverterSet
    def __init__(self):
        self.converters = []

    # adds a new converter to the set, given the line of input with it
    def addConverter(self, s: str):
        newConverter = Converter(s)
        self.converters.append(newConverter)
      
    # converts the given number like following:
    # - if there is a suitable converter for the number, then call the corresponding method and return the result
    # - return the number itself, because there is no converter for it  
    def convert(self, num) -> int:
        for c in self.converters:
            if c.isInConverter(num):
                return c.convert(num)
        return num
    
# will read a string of numbers and return a list with them
def strToList(s: str) -> List[int]:
    nums = s.split(" ")
    res = []
    for num in nums:
        res.append(int(num))
    return res

converterSets = [ConverterSet()]  # will contain the seven converter sets
seeds = [int]                   # the seeds to be converted

# opne the input file and convert its lines into a List[str]
file = open("input.txt")
lines = file.readlines()
for i in range(len(lines)):
    lines[i] = lines[i].replace("\n", "")

# read the seeds
seeds = strToList(lines[0].split(": ")[1])

# read all the converter sets and the converters inside them
i, convSetCnt = 3, 0
while i < len(lines):
    if lines[i] == "":                          # moving to the next converter set
        convSetCnt+=1
        converterSets.append(ConverterSet())    # adding an empty converter set 
        i+=2
        continue
    converterSets[convSetCnt].addConverter(lines[i])    # add a converter to the current converter set
    i+=1

minn = 1<<63
for s in seeds:
    for cs in converterSets:
        s = cs.convert(s)
    # print(s)
    minn = min(minn, s)
print(minn)
        
    