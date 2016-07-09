d = {'a':10, 'b': 20, 'c': 30}
t = d.items()
print t # print tuples for dictonary

t.sort() # print sorted version of tuple which contains list
print t
# sorted version of that list
print 'Data Sorted.....'
data_sorted = sorted(d.items())
print data_sorted
print 'Loop....'
for k, v in sorted(d.items()):
    print k, v
