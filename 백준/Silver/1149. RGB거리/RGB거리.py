n = int(input())
lst = []
for _ in range(n):
    lst.append(list(map(int, input().split())))

dp = [[0,0,0] for _ in range(n)]
dp[0][0] = lst[0][0]
dp[0][1] = lst[0][1]
dp[0][2] = lst[0][2]

for i in range(1,n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2])+lst[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2])+lst[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1])+lst[i][2]
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))