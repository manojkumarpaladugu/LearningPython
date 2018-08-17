#Python Program to Calculate the Number of Digits and Letters in a String

string = input("Enter a string:")
digits = 0
letters = 0
for i in string:
  if i >= '0' and i <= '9':
    digits += 1
  elif (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
    letters += 1
print("letters:{}, digits:{}",letters,digits)
