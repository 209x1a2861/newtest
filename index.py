'''Linked List in Python'''
class Node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
      self.head = None
    def insert(self,data):
        newnode=Node(data)
        if(self.head):
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
        else:
            self.head=newnode
    def atbegin(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode
    def atmiddle(self,middle_node,data):
        if middle_node is None:
            print("the node is not present")
            return
        newnode=Node(data)
        newnode.next=middle_node.next
        middle_node.next=newnode
        
    def print(self):
        current=self.head
        while current:
            print(current.data)
            current=current.next
            
    def remove(self,key):
        headval=self.head
        if headval.data==key and self.head!=None:
            self.head=headval.next
            headval=None
            return
        while headval.next:
            if headval.data==key:
                break
            prev=headval
            headval=headval.next
        if headval.data==None:
            return
        prev.next=headval.next
        headval=None
        
            
            
            
LL=LinkedList()
LL.insert(3)
LL.insert(4)
LL.insert(5)
LL.atbegin(10)
LL.atmiddle(LL.head.next,14)
LL.remove(3)
LL.print()
print("jghngs")
'''Linkedlist END'''



