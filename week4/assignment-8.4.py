fname = raw_input("Enter filename: ")
fhandle = open(fname)
lst = list()
for line in fhandle:
    line = line.rstrip()
    line = line.split()
    for word in line:
         if word not in lst:
            lst.append(word)
lst.sort()
print lst
