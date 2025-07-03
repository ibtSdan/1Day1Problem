n, m = map(int,input().split())
ans = []

def DFS(s):
    if len(ans)==m:
        print(' '.join(map(str, ans)))
        return
    for i in range(s,n+1):
        ans.append(i)
        DFS(i+1)
        ans.pop()
DFS(1)