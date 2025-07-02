class Stack:
    def __init__(self):
        self.items = []	# 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:	# pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:	# indexError 발생
            print("Stack is empty")
            return None

    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty")
            return None

    def __len__(self):	# len()로 호출하면 stack의 item 수 반환
        return len(self.items)
         
    def isEmpty(self):
        return len(self)== 0
    
    def __str__(self):
        return str(self.items[::1])

sequence_stack = Stack()
extra_stack = Stack()
minus_stack = Stack()

n = int(input())

sequence_list = []
answer_list = []
for i in range(n):
    sequence_list.append(int(input()))
    

cnt = 1

for i in range(1, n + 1):
    answer_list.append('+')
    if sequence_stack.isEmpty():
        sequence_stack.push(i)
        cnt += 1
    elif sequence_list[-cnt] == i:
        while not minus_stack.isEmpty():
            answer_list.append(minus_stack.pop())
        sequence_stack.push(i)
        cnt += 1
    else:
        extra_stack.push(i)
        minus_stack.push('-')
    print(sequence_stack)
    print(extra_stack)
    print(answer_list)


idx = len(extra_stack) - 1
  
while not extra_stack.isEmpty():
    print(sequence_list[idx], idx, extra_stack.top())
    if sequence_list[idx] != extra_stack.pop():
        print('NO')
        # quit()
    idx -= 1

for element in answer_list:
    print(element)