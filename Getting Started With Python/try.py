astr = "Hello"
try:
  istr = int(astr)
except:
  istr = 0
  
print "First",istr

astr = "1234"
try:
  istr=int(astr)
except:
  istr = 0 
  
print "Second",istr 
