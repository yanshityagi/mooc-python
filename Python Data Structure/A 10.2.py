lines = open('mbox-short.txt').readlines()

data = {}

def get_hour(line):
    line_split = line.split(':')
    return line_split[0].split()[-1]
    
for line in lines:
    if line.startswith('From '):
        hour = get_hour(line)
        count = data.get(hour, 0) +1
        data.update({hour:count})
        
#sorting

most = list()
for k,v in data.items():
    most.append( (k,v) )

most.sort()

for k,v in most:
    print k,v 