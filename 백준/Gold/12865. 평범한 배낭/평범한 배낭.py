n, k = map(int, input().split())
lst = []
dp = [[0 for j in range(k+1)] for i in range(n+1)]
for _ in range(n):
    lst.append(list(map(int, input().split())))
    
for i in range(1, n+1):
    w, v = lst[i-1]
    for j in range(k+1):
        if j<w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)
            
print(dp[n][k])