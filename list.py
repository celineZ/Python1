fhand = raw_input("Enter file name :")
if len(fhand) == 0:
    fhand = "romeo.txt"
    
fh = open(fhand)

inp = fh.read()

words = inp.split()
words.sort()
lst=list()
for word in words:
    if word not in lst:
        lst.append(word)
    
    

    
    
    #print line
print lst

