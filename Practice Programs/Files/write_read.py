'''
# to write a string to file
fobj = open("test.txt", 'w')
fobj.write("Hi, This is Manoj Kumar Paladugu\nWorks at AMI India")
fobj.close()

# to read a string from file
fobj = open("test.txt", "r")
buf = fobj.read()
print(buf)
fobj.close()
'''

#to write list to a file
list1 = ['Hi, This is Manoj Kumar Paladugu\n', 'Works at AMI India.']
fobj = open("test.txt",'w')
fobj.writelines(list1)
fobj.close()

#to read list from a file
fobj = open("test.txt", 'r')
list1 = fobj.readlines()
print list1
fobj.close()
