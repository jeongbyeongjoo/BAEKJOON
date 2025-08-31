N = int(input())

arr = []

for i in range(N):
    arr.append(int(input()))
    
arr_sorted = sorted(arr)

for i in range(N):
    print(arr_sorted[i])