#Python Program to Check if a Number is a Strong Number

def factorial(num):
  total = 1
  for i in range(num,0,-1):
    total *= i
  return total

def is_strong(num):
  temp = num
  total = 0
  while temp:
    total += factorial(temp%10)
    temp /= 10
  if total == num:
    return 1
  else:
    return 0

num = input("Enter a number:")
if is_strong(num):
  print("%d is a strong number" %(num))
else:
  print("%d is not a strong number" %(num))
