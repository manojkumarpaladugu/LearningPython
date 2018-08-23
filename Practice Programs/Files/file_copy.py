# Python Program to Copy the Contents of One File into Another

fobj1 = open(raw_input("Enter file1: "),'r')
fobj2 = open(raw_input("Enter file2: "),'w')

file1_content = fobj1.read()
fobj2.write(file1_content)

fobj1.close()
fobj2.close()
