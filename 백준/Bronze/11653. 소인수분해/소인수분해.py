N = int(input()) # 정수형으로 입력받는 것이 좋습니다.
i = 2

while N != 1:
    if N % i == 0:
        print(i)
        N = N // i
    else:
        i += 1