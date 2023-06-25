class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack) == 0

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)

print(stack.pop())  # Output: 30
print(stack.is_empty())  # Output: False
print(stack.pop())  # Output: 20
print(stack.pop())  # Output: 10
print(stack.is_empty())  # Output: True
print(stack.pop())  # Output: Stack is empty
