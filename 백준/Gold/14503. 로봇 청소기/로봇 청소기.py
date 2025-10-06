n, m = map(int, input().split())
x, y, d = map(int,input().split())
lst = []
for _ in range(n):
    lst.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,0,-1]

move = True
cnt = 0
while move:
    check = False
    if lst[x][y]==0:
        cnt += 1
        lst[x][y] = 2
    for k in range(4):
        nx = dx[k]+x
        ny = dy[k]+y
        if 0<=nx<n and 0<=ny<m and lst[nx][ny] == 0:
            check = True
            break
    if not check: #주변에 빈칸 없음
        if d==0:
            if x+1>=n or lst[x+1][y]==1: #뒤로 못감
                move = False
                break
            else:
                x = x+1
        elif d==1:
            if y-1<0 or lst[x][y-1]==1:
                move = False
                break
            else:
                y = y-1
        elif d==2:
            if x-1<0 or lst[x-1][y]==1:
                move = False
                break
            else:
                x = x-1
        else:
            if y+1>=m or lst[x][y+1]==1:
                move = False
                break
            else:
                y = y+1
    else: #주변에 빈칸 있음
        if d==0:
            di = [3,2,1,0]
        elif d==1:
            di = [0,3,2,1]
        elif d==2:
            di = [1,0,3,2]
        else:
            di = [2,1,0,3]
        
        for i in di:
            if 0<=x+dx[i]<n and 0<=y+dy[i]<m and lst[x+dx[i]][y+dy[i]]==0:
                x = x+dx[i]
                y = y+dy[i]
                d = i
                break

print(cnt)