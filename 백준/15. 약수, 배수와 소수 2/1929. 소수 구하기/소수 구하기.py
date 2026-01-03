import sys

input = sys.stdin.readline

m, n = map(int, input().split())

def is_prime(data):
    if (data < 2):
        return False

    result = True
    for i in range(2, int(data**0.5) +1):
        if (data % i == 0):
            result = False
            break
    
    return result

for i in range(m, n + 1):
    if is_prime(i):
        print(i)

