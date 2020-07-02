str = raw_input ("Enter a number:")

try:
  no = int(str)
except:
  no = -1
  
if no > 0:
  print "nice work"

else:
  print "Not a number"