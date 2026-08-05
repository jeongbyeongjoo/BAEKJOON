from sortedcontainers import SortedSet

n = int(input())
commands = []
x = []

sorted_set = SortedSet()

for _ in range(n):
    line = input().split()
    commands.append(line[0])
    if line[0] in ["add", "remove", "find", "lower_bound", "upper_bound"]:
        x.append(int(line[1]))
    else:
        x.append(0)

for command, elem in zip(commands, x):
    if command == 'add':
        sorted_set.add(elem)
    elif command == 'remove':
        sorted_set.remove(elem)
    elif command == 'find':
        if elem in sorted_set:
            print('true')
        else:
            print('false')
    elif command == 'lower_bound':
        if sorted_set.bisect_left(elem) < len(sorted_set):
            print(sorted_set[sorted_set.bisect_left(elem)])
        else:
            print(None)
    elif command == 'upper_bound':
        if sorted_set.bisect_right(elem) < len(sorted_set):
            print(sorted_set[sorted_set.bisect_right(elem)])
        else:
            print(None)
    elif command == 'largest':
        if sorted_set:
            print(sorted_set[-1])
        else:
            print(None)
    elif command == 'smallest':
        if sorted_set:
            print(sorted_set[0])
        else:
            print(None)
    
