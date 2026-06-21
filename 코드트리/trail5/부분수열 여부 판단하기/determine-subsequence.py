n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

def solve():
    i = 0
    for j in range(m):
        while i < n and A[i] != B[j]:
            i += 1

        if i == n:
            return False
            
        if A[i] == B[j]:
            i += 1
            continue

        
    return True

if solve():
    print("Yes")       
else:
    print("No")

