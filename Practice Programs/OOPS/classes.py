
#Class

class FirstClass:
    def set_data(self,value):
        self.data = value
    def print_data(self):
        print("FirstClass: {}".format(self.data))

x = FirstClass()
x.set_data(1.21)
x.print_data()

#end


#Second Class

class SecondClass(FirstClass):
    def set_data(self,value):
        self.data = value
    def print_data(self):
        print("SecondClass: {}".format(self.data))
class SecondClass(FirstClass):
    def print_data(self):     #Replaces print_data in FirstClass
        print("Hello World")

x = SecondClass()
x.set_data(1.21)
x.print_data()

#end

#Third Class

class ThirdClass(SecondClass): # Inherit from SecondClass
    def __init__(self, value): # On "ThirdClass(value)"
        self.data = value
    def __add__(self, other): # On "self + other"
        return ThirdClass(self.data + other)
    def __str__(self): # On "print(self)", "str()"
        return '[ThirdClass: %s]' % self.data

a = ThirdClass('abc')   # __init__ called
print(a)

b = a + 'abc'   # __add__: makes a new instance
print(b)        # __str__: returns display string

