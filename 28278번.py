import sys

class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, val):
        self.items.append(val)
        
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("stack is empty")
            return None
       
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("stack is empty")
            return None
        
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self)==0
    
data_stack = Stack()    
    
n = int(sys.stdin.readline()) # 명령의 수 입력 받기    

for i in range(n):
    input_data = sys.stdin.readline().split()
    if '1' in input_data:
        data_stack.push(input_data[-1])
        continue
    elif '2' in input_data:
        if data_stack.isEmpty():
            print(-1)
        else:
            print(data_stack.pop())
    elif '3' in input_data:
        print(len(data_stack))
    elif '4' in input_data:
        if data_stack.isEmpty():
            print(1)
        else:
            print(0)
    elif '5' in input_data:
        if data_stack.isEmpty():
            print(-1)
        else:
            print(data_stack.top())