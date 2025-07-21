T = int(input())

for i in range(T):
    C = int(input())
    quarter = C // 25 
    C %= 25
    dime = C // 10
    C %= 10
    nickel = C // 5
    C %= 5
    penny = C // 1
    print(quarter, dime, nickel, penny)
    