#Python Program to Multiply All the Items in a Dictionary

d={'A':10,'B':5,'C':10}

total = 1
for key in d:
  total *= d[key]

print(total)
