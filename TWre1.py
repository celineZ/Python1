import re

hand = open ("regex_sum_269843.txt")
inp = hand.read()

numlist = list()

words = inp.split()


stuff = re.findall("([0-9]+)", inp)
num = [int(i) for i in stuff]
  

    

count = len(stuff)
print sum(num)
print count
print sum(num)/count 



#print sum( [ ****** *** * in **********('[0-9]+',**************************.read()) ] )

# fastest way
print sum( [ int(i) for i in re.findall('[0-9]+',open("regex_sum_269843.txt").read()) ] )
