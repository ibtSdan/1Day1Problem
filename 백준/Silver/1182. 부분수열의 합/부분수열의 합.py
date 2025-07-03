n, m = map(int,input().split())
A = list(map(int,input().split()))

cnt = 0
def DFS(idx,currentSum):
    global cnt
    if idx==n:
        if currentSum==m:
            cnt += 1
        return
    DFS(idx+1,currentSum+A[idx])
    DFS(idx+1,currentSum)

DFS(0,0)

if m==0:
    cnt -= 1
print(cnt)