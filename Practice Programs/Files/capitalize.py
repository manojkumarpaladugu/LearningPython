# Python Program to Read a File and Capitalize the First Letter of Every Word in the File

'''
fobj = open(raw_input("Enter a filename: "),'r')
fobj_content = fobj.read()
flag = 0
for i in range(0,len(fobj_content),1):
  if flag == 1:
    fobj_content = fobj_content[:i] + fobj_content[i].upper() + fobj_content[i+1:]
    flag = 0   
  if fobj_content[i] == ' ' or fobj_content[i] == '\n':
    flag = 1
    
print fobj_content
'''

#another method
content = ""
with open(raw_input("Enter a filename: "),'r') as fobj:
  for line in fobj:
    content = content + line.title()

print content
