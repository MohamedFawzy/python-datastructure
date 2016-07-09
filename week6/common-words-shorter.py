name = raw_input("Enter filename: ")
try:
    fhand = open(name)
except:
    print 'File name', name,'not exist'
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
result = sorted( [ (v,k) for k,v in counts.items() ] )
result.sort(reverse=True)
print result[:10]
