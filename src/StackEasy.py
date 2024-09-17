class StackEasy:            
            
    def __init__(self):      
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.stack.pop()
    
    def peek(self):
        if self.is_empty():
            raise IndexError("La pila está vacía")
        return self.stack[-1]
    
    def size(self):
        return len(self.stack)
    
    def __str__(self):
        return str(self.stack)

pila = StackEasy()
pila.push(10)
pila.push(20)
pila.push(30)
print("Pila después de agregar elementos:", pila)
print("Elemento en el tope:", pila.peek())
print("Pila después de hacer pop:", pila.pop())
print("Tamaño de la pila:", pila.size())
print("Pila final:", pila)
