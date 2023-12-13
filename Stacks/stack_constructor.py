class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self,value):
        new_node=Node(value)
        self.top=new_node
        self.height=1

    def print_stack(self):
        temp=self.top
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def push(self,value):
        """
        This method is reponsible for adding elements to the stack.
        if stack is empty,then it will intilaze top is new_node,
        if stack is not empty,then new node will map to top node and
        then top node will update to new node.
        """
        new_node=Node(value)
        if self.height==0:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node
        self.height+=1
        return True

    def pop(self):
        if self.height == 0:
            return None
        else:
            temp = self.top
            self.top = self.top.next
            temp.next = None
            self.height -= 1
            return temp

   
    
        


        


my_stack=Stack(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(7)
my_stack.print_stack()
print()
print(my_stack.pop().value,"/n")
print()
print(my_stack.print_stack())

