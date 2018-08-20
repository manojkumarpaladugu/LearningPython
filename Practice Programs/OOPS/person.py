
class Person:
  def __init__(self,name,job=None,pay=0): #here "job" and "pay" are default
    self.name = name                      #arguements
    self.job = job
    self.pay = pay
  def GiveRaise(self, percent):
    self.pay = int(self.pay * ((percent / 100) + 1))
  def __str__(self):
    return 'Name:%s Job:%s Pay:%s'%(self.name, self.job, self.pay)

class Manager(Person):
  def GiveRaise(self, percent, bonus = 10):
    Person.GiveRaise(self, percent + bonus)

manoj = Person('Manoj Kumar','System Software Engineer',25000)
sanjeev = Person('Sanjeev Kumar', 'System Software Engineer',25000)
print (manoj)
manoj.GiveRaise(10)
print (manoj)
senthil = Manager('Senthil Kumar', 'Manager', 100000)
print(senthil)
senthil.GiveRaise(10)
print(senthil)
