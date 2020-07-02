while True:
  line =raw_input (">")
  line = line.strip()
  if line[0] == "#":
    continue
  if line == "done":
    break
  print line
print "enter" 