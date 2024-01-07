class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Queue:

    def __init__(self,value):
        node=Node(value)
        self.first=node
        self.last=node
        self.length=1

    def print_queue(self):
        temp=self.first
        while temp:
            print(temp.value)
            temp=temp.next

    def enqueue(self,value):
        node=Node(value)
        if self.first is None:
            self.first=node
            self.last=node
        else:
            self.last.next=node
            self.last=node
        self.length+=1

    def dequeue(self):
        temp=self.first
        if self.length ==0:
            return None
        if self.length==1:
            self.first=None
            self.last=None
        else:
            self.first=self.first.next
            temp.next=None
        self.length-=1
        return temp.value
q=Queue(1)
q.enqueue(2)
q.enqueue(5)
q.dequeue()

q.print_queue()