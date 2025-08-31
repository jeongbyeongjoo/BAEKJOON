import sys

N = int(sys.stdin.readline())

arr = [int(sys.stdin.readline()) for i in range(N)]

arr_sorted = sorted(arr)

sys.stdout.write('\n'.join(map(str, arr_sorted)))