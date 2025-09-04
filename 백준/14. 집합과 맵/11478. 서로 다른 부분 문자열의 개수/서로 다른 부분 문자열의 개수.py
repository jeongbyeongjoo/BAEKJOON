S = input()

data_set = set()
    
for i in range(len(S)):
    for n in range(len(S)-i):
        data_set.add(S[i:i+n+1])
    
print(len(data_set))