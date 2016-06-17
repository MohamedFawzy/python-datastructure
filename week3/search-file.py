fname = raw_input("Enter the filename: ")
try:
    fhand=open(fname,'r')
except:
    print 'file cannot be opened', fname
    exit()
count=0
for line in fhand:
    line = line.rstrip()
    if line.startswith('Subject'):
        count=count+1
print 'There were',count,'subject lines in',fname
