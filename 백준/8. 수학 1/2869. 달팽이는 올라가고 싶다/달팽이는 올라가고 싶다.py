A, B, V = map(int, input().split())
diff = A - B

day = (V - A) / diff + 1

if int(day) != float(day):
    day = int(day) + 1

print(int(day))