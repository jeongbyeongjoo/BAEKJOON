import sys

class Queue:
    def __init__(self):
        self.items = []
        self.idx = 0
        
    def enqueue(self, val):
        self.items.append(val)
    
    def dequeue(self):
        if self.idx == len(self.items):
            return
        data = self.items[self.idx]
        self.idx += 1
        return data
    
    def __len__(self):
        return len(self.items) - self.idx
    
    def isEmpty(self):
        return len(self) == 0
    
    def front(self):
        if self.idx == len(self.items):
            return
        data = self.items[self.idx]
        return data
    
    def rear(self):
        if self.idx == len(self.items):
            return
        data = self.items[-1]
        return data
        
n = int(sys.stdin.readline())

q = Queue()

for i in range(n):
    data = sys.stdin.readline().split()
    if 'push' in data:
        q.enqueue(int(data[-1]))
    elif 'pop' in data:
        if not q.isEmpty():
            print(q.dequeue())
        else:
            print(-1)
    elif 'size' in data:
        print(len(q))
    elif 'empty' in data:
        if q.isEmpty():
            print(1)
        else:
            print(0)
    elif 'front' in data:
        if not q.isEmpty():
            print(q.front())
        else:
            print(-1)
    elif 'back' in data:
        if not q.isEmpty():
            print(q.rear())
        else:
            print(-1)