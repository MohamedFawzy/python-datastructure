counter=dict()
names=['mohamed', 'ahmed', 'mohamed']
for name in names:
    counter[name] = counter.get(name, 0) + 1
print counter
