name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
counts = dict()

for line in handle:
    if line.startswith("From "):
    	time = line.split()
    	#print time
        hour = (time[5]).split(":")
        lst.append(hour[0])
        
for i in lst:
    counts[i] = counts.get(i,0) + 1
    
ltup = list()
for key, val in counts.items():
    ltup.append( (key, val))
    
ltup.sort()

for key, val in ltup:

    print key, val
