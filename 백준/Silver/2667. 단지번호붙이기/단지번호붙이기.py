import sys
from collections import deque

n = int(input())
A = []
for i in range(n):
    lst = input().strip()
    A.append([int(s) for s in lst])

dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False for _ in range(n)] for _ in range(n)]
total = 0
ans = []

def BFS(i, j):
    dq = deque()
    visited[i][j] = True
    dq.append((i,j))
    cnt = 1
    while dq:
        now = dq.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0<=x<n and 0<=y<n and not visited[x][y] and A[x][y]==1:
                visited[x][y] = True
                dq.append((x,y))
                cnt += 1
    ans.append(cnt)

for i in range(n):
    for j in range(n):
        if not visited[i][j] and A[i][j]==1:
            total += 1
            BFS(i,j)

ans.sort()
print(total)
for i in ans:
    print(i)