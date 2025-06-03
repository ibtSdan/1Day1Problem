import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    num = list(map(int,input().split()))
    lst.append(num)
dp = [[0 for j in range(n)] for i in range(n)]
dp[0][0] = lst[0][0]
if n>1:
    dp[1][0] = lst[1][0] + dp[0][0]
    dp[1][1] = lst[1][1] + dp[0][0]

for i in range(2,n):
    for j in range(1,i):
        dp[i][0] = dp[i-1][0] + lst[i][0]
        dp[i][i] = dp[i-1][i-1] + lst[i][i]
        dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + lst[i][j]
print(max(dp[n-1]))