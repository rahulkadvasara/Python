from collections import deque
# stack=deque()
# -->basic implementation

# standerd implementation
class Stack:
    def __init__(self):
        self.container=deque()
    
    def push(self,val):
        self.container.append(val)

    def pop(self):
        return self.container.pop()

    def peek(self):
        return self.container[-1]
    
    def is_empty(self):
        return len(self.container)==0
    
    def size(self):
        return len(self.container)
    
s=Stack()
s.push('www.jatland.com')
s.push('www.kdsr.com')
s.push('www.abc.com')
s.push('www.xyz.com')

print(s)
print(s.peek())

print(s.pop())

print(s.size())

print(s.is_empty())