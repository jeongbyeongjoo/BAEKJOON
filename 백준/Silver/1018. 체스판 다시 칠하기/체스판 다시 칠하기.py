import sys

N, M = map(int, sys.stdin.readline().split())

data_arr = []

for i in range(N):
    data_arr.append(sys.stdin.readline())

arr = [
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB",
"BWBWBWBW",
"WBWBWBWB"]

count_arr = []
for i in range(N-7):
    for j in range(M-7):
        count = 0
        for k in range(8):
            for l in range(8):
                if data_arr[i+k][j+l] != arr[k][l]:
                    count += 1
        count_arr.append(count)
        
if min(count_arr) < 64-max(count_arr):
    print(min(count_arr))
else: 
    print(64-max(count_arr))
