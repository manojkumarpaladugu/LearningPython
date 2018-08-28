# Program to replace a word with asterisks in a sentence

def mask_sentence(sentence,word,mask_char):
  index = 0
  while index < len(sentence):
    index = sentence.find(word,index)
    if index == -1:   #not found
      break
    sentence = sentence[0:index] + ('*' * len(word)) +  sentence[index +len(word):]
    index += len(word)    
  print sentence
      
sentence = input("Enter a sentence:")
word = input("Enter a word you want to mask in sentence:")
mask_sentence(sentence,word,'*') 
