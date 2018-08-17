#Employee classes


class Employee:
  def __init__(self, first, last, pay):  #it receives the instance as first arguement
    self.first = first
    self.last = last
    self.pay = pay

  def fullname(self):
    return "{} {}".format(self.first,self.last)
  

emp_1 = Employee("Manoj", "Kumar", 25000)
emp_2 = Employee("Sanjeev", "Madineni", 25000)

print(emp_1.fullname())         #from instance
print(Employee.fullname(emp_1)) #from class
    
