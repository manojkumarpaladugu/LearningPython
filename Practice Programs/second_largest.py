#Python Program to Find the Second Largest Number in a List


num_list = []
n = input("Enter no. of elements:")
print("Enter elements:")
for i in range(n):
  num_list.append(input())
print("Input list is: {}".format(num_list))

num_list.sort(reverse=True)
print("The reversed list is: {}".format(num_list))
print("The second largest number is: {}", num_list[1])

