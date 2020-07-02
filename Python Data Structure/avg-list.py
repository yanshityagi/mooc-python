#stores numbers
num = list()
while True:
    x = raw_input ("Enter numbers")
    x = x.strip().lower()
    if x == "done":
        break
    values = float(x)
    num.append (values)

print sum(num)/len(num)
print num

#they both are same 

#just run the program 
count = 0
total = 0 
while True:
    a = raw_input ("Enter")
    a = a.strip().lower()
    if a == "done":
        break 
    b = float(a)
    count = count + 1
    total = total + b

avg = total/count 
print avg 