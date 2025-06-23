import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = [0 * (m+1)]
for _ in range(n):
    lst = [0] + list(map(int,input().split()))
    A.append(lst)

D = [[0 for j in range(m+1)] for i in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

ans = D[1][1]
for x1 in range(1,n+1):
    for y1 in range(1,m+1):
        for x2 in range(x1,n+1):
            for y2 in range(y1,m+1):
                nSum = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]
                ans = max(ans, nSum)
print(ans)