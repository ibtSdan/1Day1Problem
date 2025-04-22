import sys
input = sys.stdin.readline

n, k = map(int, input().split())
A = []
for _ in range(n):
    num = int(input())
    if num>k:
        break
    A.append(num)
A.sort(reverse=True)
cnt = 0
i = 0
while k != 0:
    cnt += k // A[i]
    k %= A[i]
    i += 1
print(cnt)