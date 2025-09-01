import sys
N = int(sys.stdin.readline())

arr = []
for i in range(N):
    input_data = sys.stdin.readline().split()
    input_data.append(i)
    arr.append(input_data)
    
arr_sorted = sorted(arr, key=lambda p:(int(p[0]), p[2]))

for element in arr_sorted:
    sys.stdout.write(element[0] + " " + element[1] + "\n")
