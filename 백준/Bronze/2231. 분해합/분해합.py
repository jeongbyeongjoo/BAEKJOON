N = str(input())

for i in range(1, int(N)+1):
    M = str(i)
    sum = i
    for element in M:
        sum += int(element)
    if int(N) == sum:
        print(i)
        quit()
        
print(0)

