import sys

input = sys.stdin.readline
write = sys.stdout.write

N = int(input())
arr_N = list(map(int, input().split()))

dict_N = {x:0 for x in arr_N}

for element in arr_N:
    dict_N[element] += 1

M = int(input())
arr_M = list(map(int, input().split()))

for element in arr_M:
    write(str(dict_N.get(element, 0)))
    write(" ")