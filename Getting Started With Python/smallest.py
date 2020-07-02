smallest = None
print "before"
for value in [12,111,44,5,6,702,]:
    if smallest is None:
        smallest = value 
    elif value < smallest: 
        smallest = value
    print smallest, value 
    
print "After", smallest 