class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None
    
class DoubleLinkedList:
    def __init__(self,value):
        node=Node(value)
        self.head=node
        self.tail=node
        self.length=1

    def append(self,value):
        node=Node(value)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            node.prev=self.tail
            self.tail=node
        self.length+=1

    def print_LL(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next
        
    def pop(self):
        if self.length==0:
            return None
        temp=self.tail
        self.tail=self.tail.prev
        self.tail.next=None
        temp.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp

    def prepend(self,value):
        node=Node(value)
        if self.length==0:
            self.head=node
            self.tail=node
        node.next=self.head
        self.head.prev=node
        self.head=node
        self.length+=1


double_ll=DoubleLinkedList(1)
double_ll.print_LL()
print()
double_ll.append(2)
double_ll.append(3)
double_ll.append(4)
double_ll.print_LL()
print()
double_ll.prepend(7)
double_ll.pop()

print()
double_ll.print_LL()