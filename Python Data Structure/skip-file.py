handle = open("test.txt")
for line in handle:
    line = line.rstrip()
#another way of search
#skips line which don't start with God'   
    #if not line.startswith("God"):
    if not "God" in line:
#continue to find the lines that starts with God
        continue        
    print line 