from collections import deque
n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(s for s in input()))
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False for _ in range(m)] for _ in range(n)]
ans = 0
dq = deque()

def BFS(i,j):
    global ans
    visited[i][j] = True
    dq.append((i,j))
    while dq:
        x, y = dq.popleft()
        for k in range(4):
            nx = x+dx[k]
            ny = y+dy[k]
            if 0<=nx<n and 0<=ny<m and lst[nx][ny] != 'X' and not visited[nx][ny]:
                dq.append((nx, ny))
                visited[nx][ny] = True
                if lst[nx][ny] == 'P':
                    ans += 1

for i in range(n):
    for j in range(m):
        if lst[i][j]=='I':
            BFS(i,j)
            break
if ans:
    print(ans)
else:
    print("TT")