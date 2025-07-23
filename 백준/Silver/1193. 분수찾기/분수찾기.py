X = int(input())

numerator = 1
denominator = 1
level = 1
idx = 1
odd_num = True


while(1):
    if X <= idx:
        diff = idx - X
        if odd_num:
            numerator = 1 + diff
            denominator = level - diff      
        else:
            numerator = level - diff
            denominator = 1 + diff
        break                          
        
    odd_num = not odd_num
    level += 1
    idx += level
        
print(str(numerator) + "/" + str(denominator))