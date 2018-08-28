# Python program for removing i-th character from a string

print("Python program for removing i-th character from a string")
string = input("Enter a string:")
i = input("Enter i value:")
string = string[0:i] + string[i+1:]
print(string)
