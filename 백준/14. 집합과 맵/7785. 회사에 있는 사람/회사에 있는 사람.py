n = int(input())

data_set = set()
for _ in range(n):
    name, status = input().split()
    if status == "enter":
        data_set.add(name)
    else:
        data_set.remove(name)
        
data_set_sorted = sorted(data_set, reverse=True)

for element in data_set_sorted:
    print(element)