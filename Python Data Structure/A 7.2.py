fname = raw_input("Enter file name: ")
count=0
value = 0
sum=0
fh = open(fname)
#this is a loop
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : 
        continue
    pos = line.find(':')
    num = float(line[pos+1:]) #getting the num
    print num 
    sum=sum+num #adding the nums 
    print sum
    count = count+1  #counting such lines
    print count  
#it is out of the loop
print "Average spam confidence:", sum/count