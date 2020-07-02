handle = open("mbox-short.txt")
count = dict()

for line in handle:
    word = line.split()
    if line.startswith('From '): #find lines that are starting from "From "
        count[word[1]] = count.get(word[1], 0) + 1  
 # count the number of times in the lines does word[1] of each line occur 
print count 

bigcount = 0
email = ''
for k in count:
    if count[k] > bigcount: 
# it finds which email add. has occured most number of time 
        bigcount = count[k]
        email = k
print  email, bigcount




