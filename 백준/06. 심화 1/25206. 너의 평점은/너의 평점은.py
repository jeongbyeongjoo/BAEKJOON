sum = 0
count = 0
grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0}

for i in range(20):
    data = input().split()
    if data[2] == 'P':
        continue
    sum += float(data[1]) * float(grade[data[2]])
    count += float(data[1])
    
average = sum / count
print(average)