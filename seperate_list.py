#Python Program to Put Even and Odd elements in a List into Two Different Lists

def seperate_list(num_list):
  even_list = []
  odd_list = []
  for i in num_list:
    if i % 2 == 0:
      even_list.append(i)
    else:
      odd_list.append(i)
  return (even_list, odd_list)


num_list = []
n = input("Enter no. of elements:")
print("Enter elements:")
for i in range(n):
  num_list.append(input())
print("Input list is: {}".format(num_list))

(even_list, odd_list) = seperate_list(num_list)
print("Even list: {}".format(even_list))
print("Odd list: {}".format(odd_list))
