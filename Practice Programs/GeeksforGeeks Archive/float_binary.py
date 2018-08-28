# Program to convert floating point decimal numbers into its equivalent binary.

def reverse_str(ThisStr):
  rev_str = ""
  i = len(ThisStr) - 1
  while i >= 0:
    rev_str += ThisStr[i]
    i -= 1
  return rev_str

def convert_float_binary(float_num):
  integer_part = int(float_num)
  decimal_part = float_num - integer_part

  if integer_part:
    binary = ""
    while integer_part:
      binary = binary + (str(integer_part % 2))
      integer_part /= 2
    binary = reverse_str(binary)

  if decimal_part:
    binary += '.'
    while (int(decimal_part)) < 1:
      decimal_part *= 2
      binary += str(int(decimal_part))

  return binary


num = input("Enter integer or float number:")
print("Binary equivalent of integer/float number {} is: {}".format(num,convert_float_binary(num)))  
