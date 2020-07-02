foods = ["apple","banana","mango","mango","grapes","olive"]
print foods
print foods[2]
foods [2] = "cherry" 
print foods 
print "\n"
Diff = [12,"pink",12.66]
print Diff
print "\n"
Blank = []
print Blank
print "\n"
print []
print "\n"
inlist = [12,43,["Halo,Ciao"],"hello"]
print inlist 
print "\n"
print len(inlist)
print "\n"
print range(10)
print "\n"
print range(len(inlist))
print "\n"  

    #for loop and range loop
    #for food in foods:
    #   print food + " " +  "is a something we eat "
    # they both give the same output
    # unless you want to give i a value

for i in range(len(foods)):
    food = foods[i]
    print food + " " +  "is a something we eat "
print "\n"
    #concatenating the list 
c = Diff + inlist
print c
print len(c)
print "\n"
    #slicing the list
print inlist[1:]
print foods[:3]
print Diff[:]
print c[2:6]
print "\n"
    #append in list 
stuff = list()
stuff.append("chocolate")
stuff.append (24/12)
stuff.append (14)
print stuff
print "\n"
foods.append("pineapple")
print foods 
print "\n"

    #dir
#a = list()
#print type (a)
#print dir(a)

    #sorting a list 
foods.sort()
print foods
print foods[4]
print "\n"

x = ["a","c","r","e","b"]
print x
x.sort() #arrange it in alphabatical order 
print x 
print x [2]
print "\n"

y = [1,4,5,3,5,0,2]
print y
y.sort() #arrange in ascending order
print y 
print "\n"

print len(y)
print max(y)
print min(y)
print sum (y)
print sum(y)/len(y)
print "\n"

string = "Youth has wasted on the      Young"
stuff = string.split()
print stuff
print len(stuff)
print  stuff [2]

print "\nprinting words in stuff"

for word in stuff:
    print word

print "\nprinting words in foods"

for food in foods:
    print food 

print "\n"
z = "hello;ciao;hej;halo"
semi = z.split(";")
print semi
print len(semi)
print "\n"

#loop for slicing and spliting from a file 
fhand = open("test.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith ("God"):
        continue
    words = line.split()
    print words
    print len(words)
    print words[2]

print "\n"
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.rstrip()
    if not line.startswith ("From "):
        continue
    words = line.split()
    print words
    print "DAY: ",words[2]
    print words [1]
    mail = words [1]
    name = mail.split("@")            #double split
    print name 
    print "The name of the sender is ",name [0]
    print "\n"
    print "NEXT"
    print "\n"

print "THE END"
    

print "hello bye" 




