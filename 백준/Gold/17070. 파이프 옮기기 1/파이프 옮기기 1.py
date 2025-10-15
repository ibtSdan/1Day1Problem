import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))
cnt = 0

# d: 0(가로), 1(세로), 2(대각선)
def DFS(a,b,d):
    global cnt
    if a==b==n-1:
        cnt += 1
        return

    if d==0 or d==2:
        if b+1<=n-1 and lst[a][b+1] != 1:
            DFS(a,b+1,0)
    if d==1 or d==2:
        if a+1<=n-1 and lst[a+1][b] != 1:
            DFS(a+1,b,1)
    if a+1<=n-1 and b+1<=n-1 and lst[a][b+1] != 1 and lst[a+1][b] != 1 and lst[a+1][b+1] != 1:
        DFS(a+1,b+1,2)

DFS(0,1,0)
print(cnt)