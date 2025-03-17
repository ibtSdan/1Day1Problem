import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False]*(n+1)

# 그래프 입력 받기
for _ in range(m):
    u, v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

# DFS
def DFS(v):
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

cnt = 0
for i in range(1,n+1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)