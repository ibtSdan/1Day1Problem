import sys
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
A.sort(reverse=True)

ans = 0
for i in range(n):
    ans = max(ans, (i+1)*A[i])
print(ans)