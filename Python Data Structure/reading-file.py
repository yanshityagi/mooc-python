handle = open("test.txt")
whole = handle.read()
print len(whole)
#after knowing the lenght we can slice the file

print whole [100:160]
