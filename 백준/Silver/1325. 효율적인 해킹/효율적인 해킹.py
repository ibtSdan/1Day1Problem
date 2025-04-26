import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int, input().split())
A = [[] for _ in range(n+1)]
for _ in range(m):
    u,v = map(int,input().split())
    A[u].append(v)
ans = [0] * (n+1)

def BFS(x):
    visited = [False] * (n+1)
    dq = deque([x])
    visited[x] = True
    while dq:
        now = dq.popleft()
        for i in A[now]:
            if not visited[i]:
                visited[i] = True
                dq.append(i)
                ans[i] += 1
                
for i in range(1,n+1):
    BFS(i)

maxVal = max(ans)
for i in range(1, n+1):
    if ans[i] == maxVal:
        print(i, end=' ')