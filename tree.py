# User Defined data structures in python


#1. Trees(Non Linear)


class Node:
  def __init__(self, val):
    self.leftchild = None
    self.rightchild = None
    self.nodedata = val

root = Node(1)

root.leftchild = Node(2)
root.rightchild = Node(3)

root.leftchild.leftchild = Node(4)
root.leftchild.rightchild = Node(5)

def InOrd(root):
  if root:
    InOrd(root.leftchild)
    #print(root.nodedata)
    InOrd(root.rightchild)

InOrd(root)

def PreOrd(root):
  if root:
    #print(root.nodedata)
    PreOrd(root.leftchild)
    PreOrd(root.rightchild)
PreOrd(root)

def PostOrd(root):
  if root:
    PostOrd(root.leftchild)
    PostOrd(root.rightchild)
    
    print(root.nodedata)


PostOrd(root)

