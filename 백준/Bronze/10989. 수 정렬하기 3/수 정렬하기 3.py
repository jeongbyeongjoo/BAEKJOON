import sys

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())

count_arr = [0] * 10001

for i in range(N):
    input_data = int(input().strip())
    count_arr[input_data] += 1
    
for i in range(10001):
    for j in range(count_arr[i]):
        print(i)
    