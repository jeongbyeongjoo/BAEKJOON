N, M = map(int, input().split())

set_N = set(input() for x in range(N))
set_M = set(input() for x in range(M))

intersection_set = set_N.intersection(set_M)

print(len(intersection_set))
intersection_set = sorted(intersection_set)
for element in intersection_set:
    print(element)