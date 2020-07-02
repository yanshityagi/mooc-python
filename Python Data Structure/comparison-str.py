word = raw_input("Enter:")
word = word.strip() 

if word == "hello":
    print "It is Hello"

elif word < "hello":
    print "Your Word," + word + ",comes before hello."

elif word > "hello":
    print "Your Word," + word + ",comes after hello."

else :
    print "bye"