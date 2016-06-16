text = "X-DSPAM-Confidence:    0.8475"
#position = text.find(':')
#print position
#sup_position = text.find(' ', position)
#print sup_position
#print text[position+5:sup_position+10]

#short answer
position = text.find(':')
num = float(text[position+1:])
print num
