# Singly Linked List

class Node:

  def __init__(self,data,nextNode=None):
    self.data = data
    self.nextNode = nextNode


class LinkedList:

  def __init__(self,head = None):
    self.head = head

  def addFirst(self):
    data = input("Enter data:")
    newNode = Node(data,self.head)
    self.head = newNode

  def addLast(self):
    data = input("Enter data:")
    newNode = Node(data)
    if self.head == None:
      self.head = newNode
    else:
      cur = self.head
      while cur.nextNode:
        cur = cur.nextNode
      cur.nextNode = newNode

  def delFirst(self):
    if self.head:
      self.head = self.head.nextNode
    else:
      print("List is empty:")
      
  def delLast(self):
    if self.head:
      if self.head.nextNode == None:
        self.head = None
      else:
        cur = self.head
        while cur.nextNode and cur.nextNode.nextNode:
          cur = cur.nextNode
        cur.nextNode = None
    else:
      print("List is empty:")

  def delNode(self,element):
    if self.head:
      if self.head.nextNode == None:
        self.head = None
      else:
        cur = self.head
        while cur.nextNode.data != element:
          cur = cur.nextNode

  def delAll(self):
    if self.head:
      while self.head:
        self.head = self.head.nextNode

  def find(self,element):
    if self.head:
      cur = self.head
      while cur:
        if cur.data == element:
          return cur
        cur = cur.nextNode
      return None
    else:
      print("List is empty:")
      return None
    
  def printNodes(self):
    cur = self.head
    while cur:
      print(cur.data)
      cur = cur.nextNode


myList =LinkedList()

while 1:
  print(" 1: add first\n 2: add last\n 3: delete first\n 4: delete last")
  print(" 5: delete all nodes\n 6: find\n 7: print all nodes\n")
  print(" q: quit")
  n = input("Enter your choice:")
  if n == 1:
    myList.addFirst()
  elif n == 2:
    myList.addLast()
  elif n == 3:
    myList.delFirst()
  elif n == 4:
    myList.delLast()
  elif n == 5:
    myList.delAll()
  elif n == 6:
    instance = myList.find(input("Enter search element:"))
    if instance:
      print(instance.data)
  elif n == 7:
    myList.printNodes()
  elif n == 'q':
    break
