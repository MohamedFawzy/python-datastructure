fname=raw_input("Enter the filename: ")
try:
    fhandle=open(fname)
except:
    print 'file cannot be opened', fname
    exit()
count=0
result=0
for line in fhandle:
    if not line.startswith("X-DSPAM-Confidence:"): continue
    line = line.rstrip()
    count = count + 1
    result = result + float(line[20:])
print "Done"
print 'Average spam confidence:', result/count
