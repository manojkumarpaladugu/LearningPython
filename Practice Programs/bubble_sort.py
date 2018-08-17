#Bubble sort

num_list = [4,2,8,6,1]

for i in range(0,len(num_list)-1,1):
  for j in range(0, len(num_list)-i-1,1):
    if(num_list[j] > num_list[j+1]):
      temp = num_list[j]
      num_list[j] = num_list[j+1]
      num_list[j+1] = temp

print(num_list)
    
