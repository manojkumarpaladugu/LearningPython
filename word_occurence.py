#Python Program to Count the Occurrences of Given Word in a Given String Sentence

string = input("Enter a string sentence:")
word = input("Enter a word:")
string_list = string.split(' ')     #string to list conversion
cnt = 0
for i in string_list:
  if i == word:
    cnt += 1

print("{} occured {} times".format(word,cnt))
    
