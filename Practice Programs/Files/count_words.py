# Python Program to Count the Number of Words in a Text File

cnt = 0
with open(raw_input("Enter a filename:"),'r') as fobj:
  for line in fobj:
    line_list = line.split(' ')
    cnt += len(line_list)

print("Word count: {}".format(cnt))

