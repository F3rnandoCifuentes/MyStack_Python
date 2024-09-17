class Stack:
    class Node:
        def __init__(self,data):
            self.data = data
            self.next = None
            
    def __init__(self):
        self.top = None
        self._size = 0
        
    def push (self,data):
        new_node = self.Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size +=1
        
    def pop(self):
        if self.is_empty():
            raise IndexError("mal")
        pop_node =self.top
        self.top=self.top.next
        self._size -=1
        return pop_node.data
        
    def peek(self):
        if self.is_empty():
            raise IndexError("mal")
        return self.top.data
    
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
    
class Test:
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    

    print("ultimo=",stack.peek())
    print("borrado=",stack.pop())        
    print("tam = ",stack.size())
    print("vacio¿? =",stack.is_empty())