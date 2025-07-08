import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = []
for _ in range(n):
    A.append(int(input()))

ans = 0
idx = n-1
while k>0:
    if k>=A[idx]:
        ans += k//A[idx]
        k %= A[idx]
    idx -= 1

print(ans)