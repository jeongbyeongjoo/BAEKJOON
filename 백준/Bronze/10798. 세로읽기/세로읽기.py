data = []
len_data = []
result = ''
len_max = 0

for i in range(5):
    input_data = input()
    data.append(input_data)
    len_data.append(len(input_data))
    if len_max < len(input_data):
        len_max = len(input_data)

for i in range(len_max):
    for j in range(5):
        if len_data[j] > i:
            if data[j][i]:
                result += data[j][i] 
    
print(result)

    