n = list(input())

for i in range(len(n)):
    Max = i
    for j in range(i+1,len(n)):
        if n[Max] < n[j]:
            Max = j
    if n[i] < n[Max]:
        n[i], n[Max] = n[Max], n[i]
        
for i in n:
    print(i, end='')