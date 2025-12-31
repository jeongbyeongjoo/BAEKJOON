import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    data = int(input())
    
    if data <= 2:
        print(2)
        continue

    while True:
        is_prime = True
        for j in range(2, int(data**0.5) + 1):
            if data % j == 0:
                is_prime = False
                break 
        
        if is_prime: 
            print(data)
            break 
            
        data += 1 