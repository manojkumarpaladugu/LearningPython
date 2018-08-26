# Python program to copy odd lines from one file to another.

#method1
'''
fobj2 = open("test2.txt",'w')
i = 1

with open("test1.txt","r") as fobj1:
    for line in fobj1:
        if i%2 != 0:
            fobj2.write(line)
        i += 1
    
fobj1.close()
fobj2.close()
'''

#method2
fobj1 = open("test1.txt",'r')
fobj2 = open("test2.txt",'w')

contents = fobj1.readlines()

for i in range(0,len(contents),2):
    fobj2.write(contents[i])

fobj1.close()
fobj2.close()
