from stack import Stack


class Test:
    stack = Stack() 
    print(f"Is empty? [{stack.is_empty()}]")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.print_stack()
    print(f"Last attached [{stack.peek()}]")
    print(f"Poped [{stack.pop()}]")        
    print(f"Size [{stack.size()}]")
    stack.print_stack()
    print(f"Poped [{stack.pop()}]")  
    print(f"Is empty? [{stack.is_empty()}]")