from collections import deque

dx = [1,1,1,0,0,-1,-1,-1]
dy = [1,0,-1,1,-1,1,0,-1]
def BFS(i,j):
    dq = deque()
    visited[i][j] = True
    dq.append((i,j))
    while dq:
        now = dq.popleft()
        for k in range(8):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0<=x<h and 0<=y<w and not visited[x][y] and A[x][y]==1:
                visited[x][y] = True
                dq.append((x,y))
        

while True:
    w, h = map(int, input().split())
    if w==h==0:
        break
    else:
        A = []
        cnt = 0
        for _ in range(h):
            lst = list(map(int,input().split()))
            A.append(lst)
        visited = [[False for _ in range(w)] for _ in range(h)]
        for i in range(h):
            for j in range(w):
                if not visited[i][j] and A[i][j]==1:
                    cnt += 1
                    BFS(i,j)
        print(cnt)
        