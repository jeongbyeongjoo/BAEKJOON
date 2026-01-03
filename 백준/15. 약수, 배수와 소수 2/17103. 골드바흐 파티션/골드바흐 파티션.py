import sys

input = sys.stdin.readline

n = int(input())

prime_list = [True] * 1000001
prime_list[1] = False

for i in range(2, int(1000001**0.5) + 1):
    if (prime_list[i]):
        for j in range(i*2, 1000001, i):
            prime_list[j] = False

for _ in range(n):
    data = int(input())
    count = 0
    
    if (data == 4):
        count = 1
    # 나눴을 때 짝수인 경우
    elif ((data / 2) % 2 == 0): 
        i = int(data / 2 - 1)
        j = int(data / 2 + 1)
        while(i > 0 and j < data):
            if (prime_list[i] and prime_list[j]):
                count += 1
            i -= 2
            j += 2
    # 나눴을 때 홀수인 경우
    else:
        i, j = int(data / 2), int(data / 2)
        while(i > 0 and j < data):
            if (prime_list[i] and prime_list[j]):
                count += 1
            i -= 2
            j += 2
    print(count)