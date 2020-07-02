add = raw_input ("enter the email add. and date")
add= add.strip() .lower() 

x = add.find("@")
print x

y = add.find(' ',x)
print y

host = add[x+1:y]
print "The host is" + " " + host