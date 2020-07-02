name = raw_input("Enter:")
fhand = open('mbox-short.txt')
inp = fhand.read()

print len(inp)

for line in fhand:
    if line.startswith('X-DSPAM-Confidence:'):
        print line



