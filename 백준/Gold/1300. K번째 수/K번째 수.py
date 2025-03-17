n = int(input())
k = int(input())

s = 0
e = n*n
answer = 0
while s<=e:
    mid = (s+e)//2
    cnt = 0
    for i in range(1,n+1):
        cnt += min(n,mid//i)
    if cnt >= k:
        answer = mid
        e = mid - 1
    else:
        s = mid + 1
print(answer)