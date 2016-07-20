name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()
counts = dict()


for line in handle:
    if line.startswith("From "):
		inp = line.split()
        	#print inp[1]
        	lst.append(inp[1])

for word in lst:
    counts[word] = counts.get(word,0) + 1
    
bigword = None
bigcount = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
        
print bigword, bigcount