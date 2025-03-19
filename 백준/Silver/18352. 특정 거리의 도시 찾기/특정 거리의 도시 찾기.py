import sys
from collections import deque
input = sys.stdin.readline

n,m,k,x = map(int,input().split())
A = [[] for _ in range(n+1)]
for i in range(m):
    u,v = map(int,input().split())
    A[u].append(v)
   
def BFS(v):
    visited[v] = 0
    dq = deque()
    dq.append(v)
    while dq:
        now = dq.popleft()
        for i in A[now]:
            if visited[i] == -1:
                visited[i] = 1 + visited[now]
                dq.append(i)
    

visited = [-1] * (n+1)
BFS(x)
ans = []
for i in range(n+1):
    if visited[i] == k:
        ans.append(i)
        
ans.sort()
if not ans:
    print(-1)
else:
    for i in range(len(ans)):
        print(ans[i], end= ' ')