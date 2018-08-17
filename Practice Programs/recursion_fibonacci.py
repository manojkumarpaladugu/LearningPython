'''
#iterative fibonacci
import sys
def fibonacci(maximum):
   a = -1
   b = 1
   c = 0
   while c <= maximum:
        sys.stdout.write(str(c) + ' ')
        sys.stdout
        c = a + b
        a = b
        b = c
    
fibonacci(100)
'''

#recursive fibonacci
def fibonacci(n):
    if(n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

for i in range(0, 30, 1):
    print(fibonacci(i))
