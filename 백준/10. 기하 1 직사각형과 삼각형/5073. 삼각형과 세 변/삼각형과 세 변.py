while(True):
    arr = list(map(int, input().split()))
    
    if arr[0] == 0 and arr[1] == 0 and arr[2] == 0:
        break
    
    if max(arr) >= (sum(arr) - max(arr)):
        print("Invalid")
    else:
        if arr[0] == arr[1] == arr[2]:
            print("Equilateral")
        elif arr[0] == arr[1] and arr[1] != arr[2]:
            print("Isosceles")
        elif arr[1] == arr[2] and arr[2] != arr[0]:
            print("Isosceles")
        elif arr[2] == arr[0] and arr[0] != arr[1]:
            print("Isosceles")
        else:
            print("Scalene")
            