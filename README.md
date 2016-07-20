# Python1
largest = None
smallest = None
while True:
    ipt = raw_input("Enter a number: ")
    if ipt == "done" : break
        
    try:
        num = int(ipt)
    except:
        print "Invalid input"
        
    
        
    if smallest is None:
        smallest = num
    
    elif num < smallest :
        smallest = num
        
    if largest is None:
        largest = num
        
    elif num > largest :
        largest = num
      
        

print "Maximum is", largest
print "Minimum is", smallest
