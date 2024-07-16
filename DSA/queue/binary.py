from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty")
            return

        return self.buffer.pop()

    def is_empty(self):
        return len(self.buffer) == 0

    def size(self):
        return len(self.buffer)

    def front(self):
        return self.buffer[-1]

def binary(n):
    num=Queue()
    num.enqueue("1")

    for i in range(n):
        front=num.front()
        print(" ",front)
        num.enqueue(front+"0")
        num.enqueue(front+"1")

        num.dequeue()

if __name__ == "__main__":
    binary(10)