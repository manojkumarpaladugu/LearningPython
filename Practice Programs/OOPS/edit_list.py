# Python Program to Append, Delete and Display Elements of a List Using Classes


class Edit_list:
    def __init__(self):
        self.list_ = [1,2,3,4,5]
    def append_list(self,element):
        self.list_.append(element)
    def print_list(self):
        print(self.list_)

obj1 = Edit_list()
obj1.append_list(6)
obj1.print_list()
obj1.append_list(7)
obj1.print_list()
