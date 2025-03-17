import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n)]


for _ in range(m):
    u,v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

# DFS
def DFS(now, dep):
    visited[now] = True
    if dep == 5:
        print(1)
        sys.exit()
    for i in A[now]:
        if not visited[i]:
            DFS(i,dep+1)
    visited[now] = False
    
    
for i in range(n):
    visited = [False]*n
    DFS(i,1)

print(0)