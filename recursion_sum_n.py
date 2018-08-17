#Write a recursive Python function that returns the sum of the first n integers.

def sum_n(n):
    if(n == 1):
        return 1 
    return n + sum_n(n-1)

n = input("Input a number:")
print("The sum of first {0} integers is: {1}" .format(n,sum_n(n))) 
