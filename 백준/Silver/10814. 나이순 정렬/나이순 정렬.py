N = int(input())

arr = []
for i in range(N):
    input_data = input().split()
    input_data.append(i)
    arr.append(input_data)
    
arr_sorted = sorted(arr, key=lambda p:(int(p[0]), p[2]))

for element in arr_sorted:
    print(element[0], element[1])
