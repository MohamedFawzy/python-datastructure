name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
lst = list()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        words = line.split()
        lst.append(words[1])

for word in lst:
     counts[word] = counts.get(word, 0) + 1

bigCount = None
bigWord = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWord = word
        bigCount = count
print bigWord, bigCount
