# Program to check if a string contains any special character. Don't accept the string if it contains special characters

def check(string):
  for char in string:
    if not ((char >= 'a' and char <='z') or (char >= 'A' and char <= 'Z')):
      return 0
  return 1

string = input("Enter a string:")
if check(string):
  print("{} is accepted".format(string))
else:
  print("{} is not accepted".format(string))
