data = raw_input("Enter anything:")
data = data.strip()
print "Length of the entered data is",len(data)
if len(data) == 11:
    print data[3:9]
elif len(data) == 20:
    print data[12:]
elif len(data) == 5:
    print data[:]
else :
    print data [:5]

