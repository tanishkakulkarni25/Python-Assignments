#Create a program that implements a stack using a list.
#Add a method, safe_pop(), which safely removes the top element from the stack. If the stack is empty, the method should handle this condition by:
#2.1) Printing a message as "Stack is empty, nothing to pop."
#2.2) Returning None.

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
        return self.items  
    def safe_pop(self):
        if len(self.items) == 0:
            print("Stack is empty, nothing to pop.")
            return None
        return self.items.pop()

stack = Stack()
stack.push(10)
stack.push(20)
print("Pop:", stack.safe_pop())   
print("Pop:", stack.safe_pop())   
print("Pop:", stack.safe_pop())   
