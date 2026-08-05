from sortedcontainers import SortedDict

n = int(input())
arr = list(map(int, input().split()))

sd = SortedDict()

for i in range(n, 0, -1):
    sd[arr[i-1]] = i

for key, value in sd.items():
    print(key, value)
    
