# Python Program to Merge Two Lists and Sort it

list1 = []
list2 = []
n = input("Enter no.of elements for list1:")
print("Enter elements for list1:")
for i in range(n):
  list1.append(input())

n = input("Enter no.of elements for list2:")
print("Enter elements for list2:")
for i in range(n):
  list2.append(input())
  
list1.extend(list2) # merging list2 into list1
print(list1)
list1.sort()
print(list1)
