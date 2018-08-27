# Program to accept the strings which contains all vowels
'''
#method1
def is_string_vowel(string):
  vowels = {'a','e','i','o','u','A','E','I','O','U'}
  for char in string:
    if not (char=='a' or char=='e' or char=='i' or char=='o' or char=='u'):
      if not (char=='A' or char=='E' or char=='I' or char=='O' or char=='U'):
        return 0
  return 1
'''

#method2
def is_string_vowel(string):
  vowels = {'a','e','i','o','u','A','E','I','O','U'}
  for char in string:
    if char not in vowels:
      return 0
  return 1
      

string = input("Enter a string:")

if is_string_vowel(string):
  print("{} is accepted:".format(string))
else:
  print("{} is not accepted:".format(string))
