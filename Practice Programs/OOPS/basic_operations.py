# Python Program to Create a Class which Performs Basic Calculator Operations

class Basic:
    def __init__(self):
        self.a = input("Enter number:")
        self.b = input("Enter another number:")
    def add(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b

obj1 = Basic()
print("Addition of {} and {} is {}".format(obj1.a,obj1.b,obj1.add()))
print("Subtraction of {} and {} is {}".format(obj1.a,obj1.b,obj1.sub()))
print("Multiplicatoin of {} by {} is {}".format(obj1.a,obj1.b,obj1.mul()))
print("Division of {} by {} is {}".format(obj1.a,obj1.b,obj1.div()))
