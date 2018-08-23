# Python Program to Count the Number of Lines in a Text File


line_cnt = 0
with open(raw_input("Enter a filename:"),'r') as fobj:  
  for line in fobj:
    line_cnt += 1
print ("Line count: {}".format(line_cnt))
