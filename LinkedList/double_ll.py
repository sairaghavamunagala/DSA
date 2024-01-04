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

    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.head=self.head.next
            self.head.prev=None
            temp.next=None
        self.length-=1
        return temp

    def get(self,index):
        if index<0 or index>=self.length:
            return None
        temp=self.head
        if index<self.length/2:
            for _ in range(index):
                temp=temp.next
        else:
            temp=self.tail
            for _ in range(self.length-1,index,-1):
                temp=temp.prev
            
        return temp

    def set_value(self,value:int,index:int)->bool:
        temp=self.get(index)
        if temp:
            temp.value=value
            return True
        return False

    def insert(self,value:int,index:int)->bool:
        if index<0 or index>self.index>self.length:
            return False
        if index==0:
            self.prepend(value)
        if index==self.length:
            self.append(vallue)

        node=Node(value)
        before=self.get(index-1)
        after=before.next

        node.next=after
        node.prev=before
        before.next=node
        after.prev=node

        self.length+=1
        return True


double_ll=DoubleLinkedList(1)
double_ll.print_LL()
print()
double_ll.append(2)
double_ll.append(3)
double_ll.append(4)
double_ll.print_LL()
print()
print(double_ll.get(2))
print()
double_ll.set_value(0,0)
double_ll.print_LL()