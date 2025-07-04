import sys

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

def DFS(x, y):
    global cnt
    visited[x][y] = True
    cnt += 1
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny] and A[nx][ny]==1:
            DFS(nx, ny)
    

for i in range(n):
    for j in range(n):
        if not visited[i][j] and A[i][j]==1:
            total += 1
            cnt = 0
            DFS(i,j)
            ans.append(cnt)

ans.sort()
print(total)
for i in ans:
    print(i)