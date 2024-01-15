file = open("input.txt")
lines = file.readlines()    

sum = 0
for line in lines:
    l, r = 0, len(line)-2   # without the last character ('\n')
    while not line[l].isnumeric():
        l+=1
    while not line[r].isnumeric():
        r-=1
    
    sum += (ord(line[l])-ord('0'))*10+(ord(line[r])-ord('0'))
print(sum)
