import sys
input= sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int,input().split())
A = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)
    
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

total = 0
visited = [False]*(n+1)
for i in range(1,n+1):
    if not visited[i]:
        total += 1
        DFS(i)

print(total)