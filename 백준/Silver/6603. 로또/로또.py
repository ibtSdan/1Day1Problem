def DFS(suv, i):
    global n
    if len(suv)==6:
        print(' '.join(str(i) for i in suv))
    else:
        for idx in range(i+1,n):
            DFS(suv+[lst[idx]], idx)

while True:
    test = list(map(int, input().split()))
    if test[0]==0:
        break
    else:
        n = test[0]
        lst = test[1:]
        for i in range(n-5):
            DFS([lst[i]],i)
        print()