from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    dq = deque()
    visited[0][0] = True
    dq.append((0,0))
    while dq:
        now = dq.popleft()
        for k in range(4):
            x = now[0] + dx[k]
            y = now[1] + dy[k]
            if 0<=x<n and 0<=y<m and maps[x][y]!=0 and not visited[x][y]:
                visited[x][y] = True
                dq.append((x,y))
                maps[x][y] = maps[now[0]][now[1]] + 1
                
    if visited[n-1][m-1]:
        return maps[n-1][m-1]
    else:
        return -1