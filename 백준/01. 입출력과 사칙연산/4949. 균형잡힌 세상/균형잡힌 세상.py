class Stack:
    def __init__(self):
        self.items = []	# 데이터 저장을 위한 리스트 준비

    def push(self, val):
        self.items.append(val)

    def pop(self):
        try:	# pop할 아이템이 없으면
            return self.items.pop()
        except IndexError:	# indexError 발생
            # print("Stack is empty")
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
    
data_stack = Stack()    
sentence = input()

while sentence != '.':
    data_bool = 'yes'
    for element in sentence:
        if element in '([': 
            data_stack.push(element)
        elif element in ')':
            if '(' == data_stack.top():
                data_stack.pop()
            else:
                data_bool = 'no' 
        elif element in ']':
            if '[' == data_stack.top():
                data_stack.pop()
            else:
                data_bool = 'no' 
                
    while not data_stack.isEmpty():
        data_bool = 'no'
        data_stack.pop()
               
    print(data_bool)
                
 
    sentence = input()
