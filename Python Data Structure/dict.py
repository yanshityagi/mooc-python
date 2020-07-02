bag  = dict()  #made an empty dict.
bag["Gucci"] = "hello"  #added stuff in it under title 
bag["Prada"] = raw_input("ENTER:") #user input 
bag["capresse"] = 14 
bag["Ralph Lauren"] = 10
print bag 
print "\n" 
print bag["Gucci"]
print "\n" 
bag["capresse"] = bag["capresse"] - 10  #change the data
print bag 
print "\n" 
bag["Ralph Lauren"] = 12 #changing the value later
print bag 
print "\n" 
#dict. Litrals 
nana = {"hello": 2, "bye" : 3 , "Ciao" : "Italian"} #doen't have to come in the same order
print nana
print "\n" 
ciao = {} #empty dict.
print "An empty dict." , ciao
print "\n" 
print "hello" in bag 
print "\n"
#counting in dict.
count = dict()
foods = ["apple","banana","mango","mango","grapes","olive","apple","mango",]
for food in foods:
    if food not in count:
        count[food] = 1
    else:
        count[food] = count[food] + 1
print count 
print "\n" 
#get method
counts = dict()
names = ["liam","zayn","harry","niall","zayn","harry","louis","liam","zayn","niall","niall"]
for name in names:
    counts[name] = counts.get(name,0) + 1
print counts
print "\n" 
#looping through the dict.
for key in bag:
    print key, bag[key]
print "\n" 
print "dict. as a list",list(bag)
print "only keys",bag.keys()      #unless or untill you change anything  
print "only values",bag.values()  #the order of these 2 remain same 
print bag.items() #tuples
print "\n"





