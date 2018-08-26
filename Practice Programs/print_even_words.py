# Python program to print even length words in a string


string = input("Enter a string:")
string = string.split(' ')
for word in string:
    if((len(word)%2)==0):
        print(word)
