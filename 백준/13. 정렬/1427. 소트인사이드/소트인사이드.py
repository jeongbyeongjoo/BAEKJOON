N = input()

arr = []
for element in N:
    arr.append(element)
    
arr_sorted = sorted(arr, reverse=True)

for element in arr_sorted:
    print(element, end="")
