from sortedcontainers import SortedDict

n = int(input())

cmd = []
k = []
v = []

for _ in range(n):
    line = input().split()
    cmd.append(line[0])
    if line[0] == "add":
        k.append(int(line[1]))
        v.append(int(line[2]))
    elif line[0] == "remove" or line[0] == "find":
        k.append(int(line[1]))
        v.append(0)
    else:
        k.append(0)
        v.append(0)

sorted_dict = SortedDict()

for i in range(n):
    if cmd[i] == 'add':
        sorted_dict[k[i]] = v[i]        
    elif cmd[i] == 'remove':
        sorted_dict.pop(k[i])
    elif cmd[i] == 'find':
        if k[i] in sorted_dict:
            print(sorted_dict[k[i]])
        else:
            print('None')        
    elif cmd[i] == 'print_list':
        if sorted_dict:
            for key, value in sorted_dict.items():
                print(value, end=" ")
            print()
        else:
            print('None')
        
