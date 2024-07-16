from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()

    def reverse_string(self,val):
        return val[::-1]
    
s=Stack()
print(s.reverse_string("We will conquere COVID-19"))