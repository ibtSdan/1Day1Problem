from collections import deque
n, m = map(int, input().split())
A = [list(map(int, input())) for _ in range(n)]
dx = [1,-1,0,0]
dy = [0,0,1,-1]

def BFS(x,y):
    dq = deque()
    dq.append((x,y))
    while dq:
        x, y = dq.popleft()
        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y
            
            if 0<=nx<n and 0<=ny<m and A[nx][ny]==1:
                A[nx][ny] = A[x][y] + 1
                dq.append((nx,ny))
    print(A[n-1][m-1])
BFS(0,0)