# Python program to find the most occurring character and its count

def find_most_char(string):
  most_char = ''
  most_char = 0
  maxi = 0
  cnt = 0
  for i in range(0,len(string),1):
    cnt = 0
    for j in range(i,len(string),1):
      if string[i] == string[j]:
        cnt += 1
    if maxi < cnt:
      maxi = cnt
      most_char = string[i]
      most_char_cnt = maxi
  return most_char, most_char_cnt

string = input("Enter a string:")
most_char, most_char_cnt = find_most_char(string)
print("Most occuring character is \'{}' occured \'{}' times".format(most_char,most_char_cnt))
