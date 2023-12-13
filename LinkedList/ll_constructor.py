class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:
    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1

    def print_LL(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1

    def pop(self):
        if self.length==0:
            return None
        temp=self.head
        pre=self.head
        while temp.next is not None:
            pre=temp
            temp=temp.next
        self.tail=pre
        self.tail.next=None
        self.length-=1
        if self.length==0:
            self.head=None
            self.tail=None
        return temp



    def prepend(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.next=self.head
            self.head=new_node
        self.length +=1

    def popfirst(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        self.length-=1
        if self.length==0:
            self.tail=None
        return temp.value

my_linked_list=LinkedList(4)
# my_linked_list.append(3)
# my_linked_list.append(3)
my_linked_list.print_LL()
print()
# my_linked_list.prepend(1)
# my_linked_list.prepend(2)
my_linked_list.print_LL()
print()
my_linked_list.popfirst()
my_linked_list.print_LL()
