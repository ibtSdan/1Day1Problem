import sys
input = sys.stdin.readline
from collections import deque

m, n = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int,input().split())))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
dq = deque()
for i in range(n):
    for j in range(m):
        if A[i][j] == 1:
            dq.append((i,j))

while dq:
    now = dq.popleft()
    for k in range(4):
        x = now[0] + dx[k]
        y = now[1] + dy[k]
        if x>=0 and y>=0 and x<n and y<m and A[x][y]==0:
            dq.append((x,y))
            A[x][y] = A[now[0]][now[1]] + 1
            
ans = 0           
for i in range(n):
    for j in range(m):
        if A[i][j] == 0:
            print(-1)
            sys.exit()
        ans = max(ans,A[i][j])
    
print(ans-1)