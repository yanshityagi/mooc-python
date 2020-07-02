largest_number = 0
print "Before", largest_number
for the_num in [12,100,999,1000,124,]:
    if the_num > largest_number:
        largest_number = the_num
    print largest_number, the_num
print "After", largest_number