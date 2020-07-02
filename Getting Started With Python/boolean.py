found = False
print "before", found
for value in [12,13,24,13,123,144,11]:
    if value ==24:
        found = "true"
        break 
    print found, value
print "after",found 