count = 0
total = 0
print "before", count,total
for num in [1,2,3,4,5,12,55,7]:
    count = count + 1
    total = total + num
    print count, total, num
print "after",count,total, total/count