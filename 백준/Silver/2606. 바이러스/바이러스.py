import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
m = int(input())
A = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int,input().split())
    A[u].append(v)
    A[v].append(u)
    
visited = [False] * (n+1)
cnt = 0
def DFS(v):
    global cnt
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            cnt += 1
            DFS(i)

DFS(1)
print(cnt)