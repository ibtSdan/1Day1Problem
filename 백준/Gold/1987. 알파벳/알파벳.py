import sys
input = sys.stdin.readline

n, m = map(int, input().split())
lst = []
for _ in range(n):
    lst.append(list(s for s in input()))
visited = {'A':False,'B':False,'C':False,'D':False,'E':False,'F':False,
           'G':False,'H':False,'I':False,'J':False,'K':False,'L':False,
           'M':False,'N':False,'O':False,'P':False,'Q':False,'R':False,
           'S':False,'T':False,'U':False,'V':False,'W':False,'X':False,
           'Y':False,'Z':False}
ans = 1

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def DFS(x,y,cnt):
    global ans
    for k in range(4):
        nx = dx[k]+x
        ny = dy[k]+y
        if 0<=nx<n and 0<=ny<m and not visited[lst[nx][ny]]:
            ans = max(ans,cnt+1)
            visited[lst[nx][ny]] = True
            DFS(nx,ny,cnt+1)
            visited[lst[nx][ny]] = False

visited[lst[0][0]] = True
DFS(0,0,1)

print(ans)