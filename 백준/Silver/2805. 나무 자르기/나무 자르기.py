import sys
input = sys.stdin.readline

n, m = map(int, input().split())
woods = list(map(int, input().split()))
ans = 0
s = 0
e = max(woods)
while s<=e:
    mid = (s+e)//2
    total = 0
    for i in woods:
        if i>mid:
            total += i-mid
    if total<m:
        e = mid-1
    else:
        ans = max(ans, mid)
        s = mid+1
print(ans)