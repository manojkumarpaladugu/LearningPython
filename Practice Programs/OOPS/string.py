# Python Program to Create a Class in which One Method Accepts a String from the User and Another Prints it

class String:
    def __init__(self):
        self.string = ""
    def get_str(self):
        self.string = raw_input("Enter a string:")
    def put_str(self):
        print(self.string)

obj1 = String()
obj1.get_str()
obj1.put_str()
