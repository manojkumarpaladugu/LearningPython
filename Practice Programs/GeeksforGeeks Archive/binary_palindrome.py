# Python | Check if binary representation is palindrome


def check_binary_palindrome(binary):
  reverse_binary = ""
  i = len(binary) - 1
  while i >= 0:
    reverse_binary += binary[i]
    i -= 1
  if reverse_binary == binary:
    return 1
  else:
    return 0

binary = str(input("Enter a binary umber:"))
if check_binary_palindrome(binary):
  print("{} is palindrome".format(binary))
else:
  print("{} is not palindrome".format(binary))
