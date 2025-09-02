N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
arr_sorted = sorted(arr, key=lambda p: (p[1], p[0]))

for list in arr_sorted:
    for element in list:
        print(element, end=" ")
    print()