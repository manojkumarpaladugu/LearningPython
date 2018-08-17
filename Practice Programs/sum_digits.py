#Python Program to Find the Sum of Digits in a Number

def sum_digits(num):
  total = 0
  while num:
    total += num % 10
    num /= 10
  num=100
  return total

num = input("Enter a number:")
print("Sum of digits of number %d: %d" %(num,sum_digits(num)))
