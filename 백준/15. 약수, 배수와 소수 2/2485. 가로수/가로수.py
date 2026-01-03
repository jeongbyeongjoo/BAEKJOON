import sys 
import math

input = sys.stdin.readline

N = int(input())

arr = [0] * N
arr_set = set()

for i in range(N):
    arr[i] = int(input())
    
for i in range(N-1):
    diff = arr[i+1] - arr[i]
    arr_set.add(diff)
    
arr_list = list(arr_set)


if len(arr_list) == 1:
    gcd = arr_list[0]
else:
    gcd = math.gcd(arr_list[0], arr_list[1])
    for i in range(2, len(arr_list)):
        gcd = math.gcd(gcd, arr_list[i])
    
print((arr[-1] - arr[0]) // gcd - len(arr) + 1)