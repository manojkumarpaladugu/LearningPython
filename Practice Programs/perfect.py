#Python Program to Check if a Number is a Perfect Number


def is_perfect(num):
  total = 0
  for i in range(1,num,1):
    if num%i == 0:
      total += i
  if total == num:
    return 1
  else:
    return 0

num = input("Enter a number:")
if is_perfect(num):
  print("%d is a perfect number" %(num))
else:
  print("%d is not a perfect number" %(num))

