name = raw_input("Enter a file name:")
name = name.strip()
#this is called prompting a file name 
try:
    handle = open(name)
except:
    print "File not found named,"+ " " + name
    exit()

print handle
#to print the file we use for opertor
for line in handle:
    print line



