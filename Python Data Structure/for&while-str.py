# name = raw_input ("Enter name:")
# name = name.strip()
name = "yanshi yanesh"
index = 0
print ("the number of letters are",len(name))
while index < len(name):
    letter = name[index]
    print (index, letter )
    index = index + 1 

for letter in name:
    print (letter )
    

print ("The name is",name )