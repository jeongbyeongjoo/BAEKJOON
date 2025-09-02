N, M = map(int, input().split())
1
set_N = set()
set_M = set()
for _ in range(N):
    set_N.add(input())

count = 0
for _ in range(M):
    input_data = input()
    if input_data in set_N:
        count+=1
      
print(count)
    