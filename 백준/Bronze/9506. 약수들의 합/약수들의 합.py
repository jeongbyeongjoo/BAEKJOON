arr = []

while(True):
    n = int(input())
    
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            arr.append(i)
    if sum(arr) == n:
        print(str(n) + " = ", end="")
        for i in range(len(arr) - 1):
            print(arr[i], end="")
            print(" + ", end="")
        print(arr[-1])
    else:
        print(str(n) + " is NOT perfect.")
    arr.clear()
        
    