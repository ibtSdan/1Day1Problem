import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

dx = [1,-1,0,0]
dy = [0,0,1,-1]
total = 0
max_area = 0
visited = [[False for _ in range(m)] for _ in range(n)]

def BFS(i,j):
    global max_area
    dq = deque()
    dq.append((i,j))
    visited[i][j] = True
    area = 1
    while dq:
        now = dq.popleft()
        for k in range(4):
            x = dx[k] + now[0]
            y = dy[k] + now[1]
            if 0<=x<n and 0<=y<m and not visited[x][y] and A[x][y]==1:
                dq.append((x,y))
                area += 1
                visited[x][y] = True
    max_area = max(max_area, area)
    
for i in range(n):
    for j in range(m):
        if not visited[i][j] and A[i][j]==1:
            BFS(i,j)
            total += 1
            
print(total)
print(max_area)