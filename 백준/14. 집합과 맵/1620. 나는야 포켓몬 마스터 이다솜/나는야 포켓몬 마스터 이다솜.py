import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data_dict1 = {}
data_dict2 = {}
for i in range(1, N+1):
    input_data = input().strip()
    data_dict1[i] = input_data
    data_dict2[input_data] = i    

for _ in range(M):
    input_data = input().strip()
    if input_data.isdigit():
        print(data_dict1[int(input_data)])
    else: # 문자열일 때
        print(data_dict2.get(input_data))        