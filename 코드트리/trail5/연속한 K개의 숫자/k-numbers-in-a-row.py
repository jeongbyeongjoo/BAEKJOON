# 41분 15초

n, k, b = map(int, input().split())

num_arr = [1 for i in range(n+1)]
sum_arr = [0]*(n+1)

num_arr[0] = 0

for i in range(b):
    data = int(input())
    num_arr[data] = 0

sum_arr[1] = num_arr[1]
for i in range(2, n+1):
    sum_arr[i] = sum_arr[i-1] + num_arr[i]

max_int = 0
j = k
i = 0
while(j < n+1):
    max_int = max(max_int, sum_arr[j] - sum_arr[i])
    i += 1
    j += 1

if k - max_int > 0:
    print(k - max_int)
else:
    print(0)