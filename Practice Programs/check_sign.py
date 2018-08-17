#Python Program to Check Whether a Number is Positive or Negative
'''
#method_1
import sys

num = input("Enter a number:")
if num>0:
  print("%d is a positive number" %(num))
else:
  print("%d is a negative number" %(num))
'''

#method_2
import sys
num = input("Enter a number:")
num_size = sys.getsizeof(num)
if num>>num_size & 1:
  print("%d is a negative number" %(num))
else:
  print("%d is a positive number" %(num))
