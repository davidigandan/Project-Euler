import numpy as np
import time
start_time = time.time()



array=np.loadtxt(open("problem81_matrix.txt", "r"), delimiter=",")
array=array.astype('int16')
#print(array)


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.down = None
        self.left = None
        self.up = None
        

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


    

mylist=linked_list()


for element in array:
    for sub_element in element:
        mylist.insertEnd(Node(element))

mylist.traversal()
#runtime printer
print("--- %s seconds ---" % (time.time() - start_time))