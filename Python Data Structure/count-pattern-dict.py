
counts = dict()
line = raw_input("Enter a line")
line = line.strip().lower()
words = line.split()
print "Words as different strings", words
for word in words:
    counts[word] = counts.get(word,0) + 1
print "counts",counts


