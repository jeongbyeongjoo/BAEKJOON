N = int(input())

arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    
arr_sorted = sorted(arr)

for list in arr_sorted:
    for element in list:
        print(element, end=" ")
    print()