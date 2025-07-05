import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))
    
s = 1
e = max(A)
ans = s
while s<=e:
    mid = (s+e)//2
    currentSum = 0
    for i in A:
        currentSum += i//mid
    if currentSum<k:
        e = mid - 1
    elif currentSum>=k:
        ans = max(ans, mid)
        s = mid + 1
print(ans)