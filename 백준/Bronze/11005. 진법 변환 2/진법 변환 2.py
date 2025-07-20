N, B = map(int, input().split())
idx = 0

while(1):
    if N >= pow(B, idx):
        idx += 1
    else:
        if idx != 0:
            idx -=1
        break

for i in range(idx, -1, -1):
    data = N // pow(B, i)    
    N = N % pow(B, i)
    if data < 10:
        print(data, end="")
    else:
        print(chr(data+55), end="")
