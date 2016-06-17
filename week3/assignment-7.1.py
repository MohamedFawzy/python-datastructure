# Use words.txt as the file name
fname = raw_input("Enter file name: ")
try:
    fhandle = open(fname)
except:
    print 'file cannot be opened', fname
    exit()
for line in fhandle:
   line = line.rstrip()
   print line.upper()
