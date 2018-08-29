# Python program to count number of vowels using sets in given string

def count_vowels(string):
  cnt = 0
  vowels = set("aeiouAEIOU")
  for alphabet in string:
    if alphabet in vowels:
        cnt += 1
  return cnt

string = input("Enter a string:")
print("Vowel count in string \"{}\": {}".format(string,count_vowels(string)))
