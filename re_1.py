import re

hand = open ("regex_sum_269843.txt")
numlist = list()
count = 0
for line in hand:
    line = line.rstrip()
    stuff = re.findall(([0-9.]+), line)
    count = count + 1
    num = int(stuff)
    numlist.append(num)

print sum(numlist)/count    
