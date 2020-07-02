greet = "hello you"
a = raw_input("Enter name")
a = a.lstrip() .rstrip()
greet = greet.replace("you",a)
greet = greet.upper()
print greet 

hey = greet.find("I")
print hey, "found it"
