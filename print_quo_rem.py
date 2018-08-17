#Python Program to Read Two Numbers and Print Their Quotient and Remainder

num1 = input("Enter number_1:")
num2 = input("Enter number_2:")
if num1 > num2:
  quotient = num1 / num2
  remainder = num1 % num2
else:
  quotient = num2 / num1
  remainder = num2 % num1

print("Quotient: %d" %(quotient))
print("Remainder: %d" %(remainder))
