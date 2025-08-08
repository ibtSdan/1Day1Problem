n, m = map(int, input().split())
ans = []
ans.extend(list(map(int,input().split())))
ans.extend(list(map(int,input().split())))
ans.sort()
for i in ans:
    print(i, end=' ')