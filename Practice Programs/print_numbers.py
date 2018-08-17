#Python Program to Print all Numbers in a Range Divisible by a Given Number


print("Please input minimum and maximum ranges")
mini = input("Enter minimum:")
maxi = input("Enter maximum:")
divisor = input("Enter divisor:")

for i in range(mini,maxi+1,1):
  if i % divisor == 0:
    print("%d" %(i))
