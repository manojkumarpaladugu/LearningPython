#Python Program to Find the Largest Number in a List


num_list = []
n = input("Enter no. of elements:")
print("Enter elements")
for i in range(n):
  num = input()
  num_list.append(num)
print("Input list is: {}".format(num_list))

big = 0
for i in num_list:
  if i > big:
    big = i

print("Largest number in the list is: {}".format(big))
