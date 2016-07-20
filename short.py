# Use the file name mbox-short.txt as the file name
fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = "mbox-short.txt"
fh = open(fname)
count = 0
wmun = 0
for line in fh:
    
    if not line.startswith("X-DSPAM-Confidence:") : continue
    #print line
    count = count + 1
    
    
    num =  float(line[20:])
    wmun = wmun + num
ave = wmun/count
    #print ave
print "Average spam confidence:", ave