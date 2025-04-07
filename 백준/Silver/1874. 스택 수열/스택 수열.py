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
            # print("Stack is empty")
            return None

    def __len__(self):	# len()로 호출하면 stack의 item 수 반환
        return len(self.items)
         
    def isEmpty(self):
        return len(self)== 0
    
    def __str__(self):
        return str(self.items[::1])

sequence_stack = Stack()
answer_list = []
first_data_list = []
seconde_data_list = []

n = int(input())
idx = 1

for i in range(n):
    data = int(input())
    seconde_data_list.append(data)
    if sequence_stack.top() != data:
        for j in range(idx, data + 1):
            sequence_stack.push(j)
            answer_list.append('+')
            idx += 1
    first_data_list.append(sequence_stack.pop())
    answer_list.append('-')
    
if first_data_list != seconde_data_list:
    print('NO')
else: 
    for element in answer_list:
        print(element)

