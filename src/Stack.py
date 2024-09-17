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
    
    def print_stack(self):
        if self.is_empty():
            print("La pila está vacía")
        else:
            current_node = self.top
            while current_node is not None:
                print(current_node.data, end=" -> ")
                current_node = current_node.next
            print("None") 
    
class Test:
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    stack.print_stack()
    print(f"Last attached [{stack.peek()}]")
    print(f"Poped [{stack.pop()}]")        
    print(f"Size [{stack.size()}]")
    print(f"Empty? [{stack.is_empty()}]")