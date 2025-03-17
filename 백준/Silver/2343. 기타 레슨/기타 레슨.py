import sys
input = sys.stdin.readline

n,m = map(int,input().split())
lst = list(map(int,input().split()))

s = max(lst)
e = sum(lst)
answer = e

while s<=e:
    mid = (s+e)//2
    cnt = 1
    temp = 0
    
    for i in lst:
        if temp + i > mid:
            cnt += 1
            temp = 0
        temp += i
    if cnt > m:
        s = mid + 1
    else:
        answer = mid
        e = mid - 1
print(answer)