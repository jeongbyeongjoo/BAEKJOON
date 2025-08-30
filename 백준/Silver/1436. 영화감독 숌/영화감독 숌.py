N = int(input())

arr = []

count = 0
while(True):
    count += 1
    str_count = str(count)
    if "666" in str_count:
        arr.append(count)
        if len(arr) == N:
            print(arr[-1])
            break