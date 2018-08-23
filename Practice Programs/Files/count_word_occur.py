# Python Program to Count the Occurrences of a Word in a Text File


cnt = 0
word = raw_input("Enter a word: ")
with open(raw_input("Enter a filename:"),'r') as fobj:
  for line in fobj:
    line_list = line.split(' ')
    for i in line_list:
      if i == word:
        cnt += 1
        
print("{} appeared {} times".format(word,cnt))
