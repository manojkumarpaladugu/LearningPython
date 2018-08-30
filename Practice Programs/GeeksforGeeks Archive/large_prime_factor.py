# Python Program for to Find largest prime factor of a number

def is_prime(num):
  for i in range(2, (num / 2) + 1, 1):
    if num % i == 0:
      return 0
  return 1

def find_largest_prime_factor(num):
  maxi = 0
  for i in range(1, (num / 2) + 1, 1):
    if num % i == 0:
      if is_prime(i):
        if maxi < i:
          maxi = i
  return maxi

num = input("Enter a number:")
print find_largest_prime_factor(num)
