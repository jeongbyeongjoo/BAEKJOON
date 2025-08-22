arr = []

for i in range(3):
    n = int(input())
    arr.append(n)
    
if sum(arr) == 180:
    if arr[0] == 60 and arr[1] == 60 and arr[2]:
        print("Equilateral")
    elif (arr[0] == arr[1]) or (arr[1] == arr[2]) or (arr[2] == arr[0]):
        print("Isosceles")
    else:
        print("Scalene")        
else:
    print("Error")
    