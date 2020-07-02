
def greet(l):
   
   l = l.strip().lower() 
   if l == "es":
      print ("HOLA")
   elif l =="fr":
      print ("BONJOUR")
   elif l =="hi":
      print ("NAMASTE")
   elif l == "dn":
      print ("HEJ")
   elif l == "it":
      print ("CIAO")
   else:
      print ("HELLO")
  

lang = input("Enter lang.")

greet(lang)