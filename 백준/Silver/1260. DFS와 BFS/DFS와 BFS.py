import sys
from collections import deque
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# DFS
def DFS(v):
    print(v, end=' ')
    visited[v] = True
    for i in A[v]:
        if not visited[i]:
            DFS(i)

# BFS
def BFS(v):
    dq = deque()
    dq.append(v)
    visited[v] = True
    while dq:
        now = dq.popleft()
        print(now, end=' ')
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)


# 입력
n, m, s = map(int, input().split())
A = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int, input().split())
    A[u].append(v)
    A[v].append(u)

for i in range(n+1):
    A[i].sort()
visited = [False] * (n+1)
DFS(s)
print()
visited = [False] * (n+1)
BFS(s)