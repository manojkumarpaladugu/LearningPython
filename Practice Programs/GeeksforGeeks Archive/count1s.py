# Length of the Longest Consecutive 1’s in Binary Representation of a given integer

def cnt_consecutive_1s(num):
  binary = str(bin(num))
  binary = binary[2:] #remove the first two characters
  print binary
  maxi = 0
  i = 0
  while i < len(binary):
    i = binary.find('1',i)
    if i == -1:
      break
    cnt = 0
    while (i < len(binary)) and (binary[i] != '0'):
      cnt += 1
      i += 1
    if maxi < cnt:
      maxi = cnt
    i += 1
  return maxi
    
  
num = input("Enter any number:")
print(cnt_consecutive_1s(num))
