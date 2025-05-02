import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
A = [[] for _ in range(n+1)]
for _ in range(n-1):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)        
visited = [False] * (n+1)
ans = [0] * (n+1)
        
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            ans[i] = v
            DFS(i)
                
DFS(1)

for i in range(2,n+1):
    print(ans[i])