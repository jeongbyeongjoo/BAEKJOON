import math

M = int(input())
N = int(input())      
    
arr = []

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(math.sqrt(x)) +1):
        if x % i == 0:
            return False
    return True
    
for i in range(M, N + 1):
    if is_prime(i):
        arr.append(i)
        
if len(arr) == 0:
    print(-1)
else:
    print(sum(arr))
    print(arr[0])            