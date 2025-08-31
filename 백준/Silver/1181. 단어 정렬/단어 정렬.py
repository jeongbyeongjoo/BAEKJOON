N = int(input())

arr = []

for i in range(N):
    input_data = input()
    if input_data in arr:
        continue
    else:
        arr.append(input_data)
        
arr_sorted = sorted(arr, key=lambda p:(len(p), p))

print("\n".join(arr_sorted))