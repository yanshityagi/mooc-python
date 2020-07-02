largest_number = 0
print "Before", largest_number
for the_num in [12,24,36,13,10,99,101]:
    if the_num > largest_number:
        largest_number = the_num
    print largest_number, the_num
print "After", largest_number