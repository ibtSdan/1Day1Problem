test = int(input())
for _ in range(test):
    n = int(input())
    dp = [0]*(n+1)
    if n<=3:
        print(1)
    else:
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        for i in range(4,n+1):
            dp[i] = dp[i-3]+dp[i-2]
        print(dp[n])