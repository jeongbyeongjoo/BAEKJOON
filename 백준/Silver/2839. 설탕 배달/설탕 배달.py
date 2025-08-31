N = int(input())

count_3 = 0
count_5 = 0

if N == 4 or N == 7:
    print(-1)
    quit()

while(True):
    if N % 5 == 0:
        count_5 += N//5
        break
    else:
        N -= 3
        count_3 += 1

print(count_3 + count_5)