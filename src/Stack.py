from node import Node
class Stack:
            
    def __init__(self):
        self.top = None
        self._size = 0
        
    def push (self,data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size +=1
        
    def pop(self):
        if self.is_empty():
            raise IndexError("Stack empty")
        pop_node =self.top
        self.top=self.top.next
        self._size -=1
        return pop_node.data
        
    def peek(self):
        if self.is_empty():
            raise IndexError("Stack empty")
        return self.top.data
    
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
    
    def print_stack(self):
        if self.is_empty():
            print("Stack empty")
        else:
            current_node = self.top
            while current_node is not None:
                print(current_node.data)
                current_node = current_node.next
