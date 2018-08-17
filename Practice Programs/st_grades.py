#Python Program to Take in the Marks of 5 Subjects and Display the Grade

def student_grade():
  marks_list = []
  print("Enter subject marks")
  for i in range(1,6,1):
    num = input("Subject[%d]:" %(i))
    marks_list.append(num)
    total = sum(marks_list)
    percentage = (total / 5)
    if percentage >= 75:
      print("Student Grade: A")
    elif percentage >= 45 and percentage < 75:
      print("Student Grade: B")
    else:
      print("Student Grade: C")

student_grade()
