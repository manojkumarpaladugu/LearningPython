'''
#Iterative factorial method
def factorial(n):
    fact = 1
    while n:
        fact *= n
        n -= 1
    return fact

n = input("Input a number:")
print("The factorial of ", n, "is ", factorial(n))
'''

#Recursive factorial method
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

n = input("Input a number:")
print("The factorial of ", n, "is ", factorial(n))
