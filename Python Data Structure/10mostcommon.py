handle = open("test.txt")
count = dict()

for line in handle:
    words = line.split()
    for word in words:
        count[word] = count.get(word,0) + 1

most = list()
for k,v in count.items():
    most.append( (v,k) )

most.sort(reverse = True)

for v,k in most[:10]:
    print k,v 

#shorter version of sorting (adv)
c = {"hello": 25, "ciao" : 20, "hej" : 45, "salut" : 25}
print sorted ( [ (v,k) for k,v in c.items() ] )
