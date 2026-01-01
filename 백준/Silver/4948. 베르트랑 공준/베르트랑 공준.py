import sys

input = sys.stdin.readline

def is_prime(data):
    if (data < 2):
        return False

    result = True
    for i in range(2, int(data**0.5) +1):
        if (data % i == 0):
            result = False
            break
    
    return result

prime = [0] * 246913

for i in range(1, 246913):
    if is_prime(i):
        prime[i] = i

while(True):
    n = int(input())
    if (n == 0):
        break
    count = 0
    for i in range(n+1, 2*n + 1):
        if (prime[i] > 0):
            count += 1
    print(count)



