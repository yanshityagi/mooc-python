hrs = raw_input ("Enter Hours")
rt = raw_input ("Enter your rate")
try:
   hrs = int(hrs)
   rt = int(rt)
   if hrs <= 40: 
      pay = hrs * float(rt)
      print int (pay)
   else:
      pay = 40 * float(rt) + (hrs - 40)  * 1.5 * float(rt)
      print float (pay)
except :
   print "ENTER A NUMBER"
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 
 
 