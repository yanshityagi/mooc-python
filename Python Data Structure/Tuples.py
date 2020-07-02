#you cannot change the value
#you cannot add any new value
#Tuples start and end with ().
tup = (1,3,"hello")
print tup
print tup[2]
print "\n"
#you can put tuple on the left hand side too without ()
(a,b) = (100,99)
hello,good = ("salut","bien")
print a,b,hello,good
print "\n"
#comparision
#goes from right to left, if first does the magic then it ignores the rest 
y = (0,1,2,3) > (0,1,2,55)
x =  ("apple","mayo","zebra") < ("apple","mona","a")
print y,x
print "\n"
#we can sort 
d = {"hello": 25, "ciao" : 20, "hej" : 45, "salut" : 25}  #capital is consider bigger than lower case
t = d.items()
print t 
t.sort()        #only looks it key #can also use sorted(d.items()) also 
print t 
print "\n" 
for k,v in sorted(d.items()): #alphabatical sorted 
    print k,v  
print "\n" 
#sort by values
val = list() #tempory list 
for k,v in d.items():
    val.append ( (v,k) ) #adding value to list 
print val
val.sort(reverse = True) #from biggest to smallest 
print val
print "\n" 
     