import sys

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
arr = list(map(int, input().split()))

arr_sorted = sorted(arr)
dict = {value : idx for idx, value in enumerate(arr_sorted)}
dict_sorted = {value : idx for idx, value in enumerate(dict)}

for element in arr:
   write(str(dict_sorted[element]))
   write(" ")