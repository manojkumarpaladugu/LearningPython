# Python Program to Read a String from the User and Append it into a File


fobj = open(raw_input("Enter filename: "),'a')
string = raw_input("Enter a string: ")
fobj.write(string)
fobj.close
