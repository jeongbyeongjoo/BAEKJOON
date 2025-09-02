data = input().split()

N = data[0]
B = int(data[1])
sum = 0


for i in range(len(N)):
    if N[-(i+1)].isalpha():
        sum += (ord(N[-(i+1)])-55) * pow(B,i)
    else:
        sum += int(N[-(i+1)]) * pow(B,i)

print(sum)