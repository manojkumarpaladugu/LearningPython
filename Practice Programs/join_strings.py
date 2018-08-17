#Python Program to Form a New String Made of the First 2 and Last 2 characters From a Given String


string = input("Enter a string:")
new_string = string[0:2] + string[len(string)-2:]
print(new_string)
