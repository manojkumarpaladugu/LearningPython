#Python Program to Check Whether a Given Year is a Leap Year

year = input("Enter a year:")
if((year%4==0 and year%100!=0) or year%400==0):
  print("%d is leap year" %(year))
else:
  print("%d is not leap year" %(year))
