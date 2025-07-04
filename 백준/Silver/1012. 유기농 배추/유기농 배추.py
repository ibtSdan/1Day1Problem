import sys
from collections import deque
input = sys.stdin.readline

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(i,j):
    dq = deque()
    dq.append((i,j))
    visited[i][j] = True
    while dq:
        now = dq.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0<=x<n and 0<=y<m and not visited[x][y] and A[x][y]==1:
                visited[x][y] = True
                dq.append((x,y))

test = int(input())
for _ in range(test):
    m, n, cabbage = map(int,input().split())
    A = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(cabbage):
        j, i = map(int,input().split())
        A[i][j] = 1
    visited = [[False for _ in range(m)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j] and A[i][j]==1:
                BFS(i,j)
                cnt += 1
    print(cnt)