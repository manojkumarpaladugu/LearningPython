#Python Program to Reverse a Given Number
'''
#method_1
def rev_num(n):
  temp = 0
  while n:
    temp *= 10
    temp += n%10
    n /= 10
  return temp
    
n = input("Enter a number:")
print("Reverse of %d is %d" %(n,rev_num(n)))
'''

#method_2

def reverse_num(num):
  temp = ""
  for i in range(len(num)-1,-1,-1):
    temp += num[i]
  return int(temp)

num = input("Enter a number:")
print("Reverse of %d is %d" %(num,reverse_num(str(num))))
