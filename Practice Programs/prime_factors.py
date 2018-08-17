#Python Program to Compute Prime Factors of an Integer

def is_prime(num):
  i = 0
  if num == 2:
    return 1
  for i in range(2,num):
    if num%i==0:
      return 0
  return 1

num = input("Enter a number:")
print("The prime factors of %d are" %(num))
for i in range(2,num/2+1,1):
  if num%i == 0:
    if is_prime(i):
      print(i)
