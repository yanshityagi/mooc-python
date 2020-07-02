name = raw_input("Enter a file name:")
name = name.strip()
try:
    handle = open(name)
except:
    print "File not found named,"+ " " + name
    exit()
count = 0 
    
for line in handle:
    count = count + 1

print "Total number of lines:",count 
