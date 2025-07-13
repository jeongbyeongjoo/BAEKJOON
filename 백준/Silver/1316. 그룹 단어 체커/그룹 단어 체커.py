n = int(input())
count = 0

for i in range(n):
    A = set()
    data = input()
    for j in range(len(data)):
        if data[j] in A :
            if data[j]!=data[j-1]:
                count -= 1
                break
        A.add(data[j])
    count += 1
        
print(count)