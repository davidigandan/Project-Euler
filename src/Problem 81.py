import numpy as np

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        

class linked_list:
    def __init__(self):
        self.head=None
        self.count=0

    def insertEnd(self, newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode

    def insertHead(self, newNode):
        tempNode = self.head
        self.head = newNode         
        self.head.next = tempNode        
        #del tempNode

    def deleteEnd(self):
        lastNode=self.head
        while lastNode.next is not None:
            prevNode=lastNode
            lastNode=lastNode.next
        prevNode.next=None

    def traversal(self):
        currentNode=self.head
        while currentNode is not None:
            print(currentNode.data)
            currentNode=currentNode.next
    
    
FirstNode=Node(2)
mylist=linked_list()
mylist.insertEnd(FirstNode)

SecondNode=Node(3)
mylist.insertEnd(SecondNode)

ThirdNode=Node(4)
mylist.insertEnd(ThirdNode)

FourthNode=Node(1)
mylist.insertHead(FourthNode)

mylist.deleteHead()
mylist.traversal()

