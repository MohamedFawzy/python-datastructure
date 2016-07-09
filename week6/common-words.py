# get top ten most common words in text file

name = raw_input("Enter filename: ")
try:
    fhand = open(name)
except:
    print 'File name', name ,'not exist'
    exit()
counts = dict()
for line in fhand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word,0) + 1
lst = list()
for key, val in counts.items():
    lst.append( (val, key) )
lst.sort(reverse=True)
for val,key in lst[:10]:
    print  key, val
