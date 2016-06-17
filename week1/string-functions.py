__author__ = 'mohamed fawzy'

s = 'Monty Python'
print s[0:4] # print from index zero to 4 but index four not included so it will print index from 0 to 3

print s[3:] # print from index 3 to the end of string

print s[:5] # print from index 5 to the begining

fruit = 'apple'
print 'n' in fruit # return boolean
print 'a' in fruit # return boolean

# string contact
a='hello'
b= a + 'world'
print b

c = a + ' ' + 'There'
print c

name = 'Mohamed FAWZY'
print name.lower() # to lower case
print 'HEY'.upper() + ' '+ name.lower()

#search string
pos = fruit.find('le') # return position for element in string index
pos1 = fruit.find('z')
print pos
print pos1 # -1 in case not exist in string
name2 = name.replace('Mohamed', 'User') # replace string with another one
print name2

greet = '  Hello Foozy ! '
print greet.lstrip() # remove space from leftside
print greet.rstrip()  # remove space from rightside
print greet.strip() # remove spaces from right and leftisde

line = 'Please have a nice day'
print line.startswith('Please')
print line.startswith('p')

data = "From mohamed@example.com Sat Jan 5 06:14:16 2016"

position = data.find('@')
print position

sppos = data.find(' ', position)
print sppos

host = data[position+1:sppos]
print host
