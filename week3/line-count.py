fhand = open('mbox-short.txt')
count=0
for line in fhand:
    count = count+1
print 'Line count ', count

fhand2 = open('mbox-short.txt')
inp = fhand2.read()
print len(inp)
print inp[:20] # read from index zero to 19
