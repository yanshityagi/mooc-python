handle = open("test.txt")
for line in handle:
    line = line.rstrip()
    if line.startswith("God"):
        print line 
