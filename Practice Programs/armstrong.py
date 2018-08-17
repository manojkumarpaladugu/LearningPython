#Python Program to Check if a Number is an Armstrong Number

def count_digits(num):
  temp = 0
  while num:
    temp += 1
    num /= 10
  return temp

def is_armstrong(num):
  cnt = count_digits(num)
  temp = num
  total = 0
  while temp:
    total += pow(temp%10, cnt)
    temp /= 10
  if(total == num):
    return 1
  else:
    return 0

num = input("Enter a number:")
if is_armstrong(num):
  print("%d is armstrong number" %(num))
else:
  print("%d is not armstrong number" %(num))
