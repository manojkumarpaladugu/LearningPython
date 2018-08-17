#Python Program to Check if a Number is a Palindrome

def is_palindrome(num):
  rev_num = 0
  temp = num
  while temp:
    rev_num = (rev_num*10)+(temp%10)
    temp /= 10
  if rev_num == num:
    return 1
  else:
    return 0

num = input("Enter a number:")
if is_palindrome(num):
  print("%d is palindrome" %(num))
else:
  print("%d is not palindrome" %(num))
