# Python Program to Find the Area of a Rectangle Using Classes

class Rectangle:
    def __init__(self):
        self.length = input("Enter length:")
        self.width = input("Enter width:")
    def cal_area(self):
        return self.length * self.width

area1 = Rectangle()
print("Area is: {}".format(area1.cal_area()))
