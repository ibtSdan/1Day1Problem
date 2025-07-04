import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())
A = []
for _ in range(n):
    lst = list(map(int,input().split()))
    A.append(lst)
dx = [1,-1,0,0]
dy = [0,0,1,-1]
visited = [[False for _ in range(m)] for _ in range(n)]
ans = []
    
def DFS(x,y):
    global cnt
    cnt += 1
    visited[x][y] = True
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny] and A[nx][ny]==1:
            DFS(nx,ny)

total = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and A[i][j]==1:
            total += 1
            cnt = 0
            DFS(i,j)
            ans.append(cnt)
            
print(total)
print(max(ans) if ans else 0)