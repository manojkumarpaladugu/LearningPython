#Python Program to Count the Number of Digits in a Number

def count_digits(num):
  count = 0
  while num:
    num /= 10
    count += 1
  return count

num = input("Enter a number:")
print("The count of digits of number %d: %d" %(num,count_digits(num)))
