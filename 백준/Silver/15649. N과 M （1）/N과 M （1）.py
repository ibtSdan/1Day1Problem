n, m = map(int,input().split())
ans = []
visited = [False] * (n+1)

def DFS():
    if len(ans)==m:
        print(' '.join(map(str,ans)))
        return
    for i in range(1,n+1):
        if not visited[i]:
            visited[i] = True
            ans.append(i)
            DFS()
            ans.pop()
            visited[i] = False
            
DFS()