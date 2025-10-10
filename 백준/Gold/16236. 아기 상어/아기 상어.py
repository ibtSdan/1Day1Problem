from collections import deque

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if lst[i][j]==9:
            s = i
            e = j
            lst[i][j] = 0
            
def BFS(i,j,size):
    dq = deque()
    dq.append((i,j,0))
    fish = []
    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[i][j] = True

    while dq:
        x, y, dist = dq.popleft()
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = dx+x
            ny = dy+y
            if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
                if lst[nx][ny]<=size:
                    visited[nx][ny] = True
                    if 0<lst[nx][ny]<size:
                        fish.append((dist+1,nx,ny))
                    dq.append((nx,ny,dist+1))
    return sorted(fish)

time, size, eat = 0,2,0
while True:
    result = BFS(s,e,size)
    if not result:
        break
    dist, x, y = result[0]
    lst[x][y] = 0
    time += dist
    eat += 1
    if eat==size:
        size += 1
        eat = 0
    s, e = x, y

print(time)