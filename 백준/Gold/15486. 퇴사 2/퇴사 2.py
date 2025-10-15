import sys
input = sys.stdin.readline

n = int(input())
lst = [(0,0)]
for _ in range(n):
    lst.append(list(map(int, input().split())))

dp = [0]*(n+2)
for i in range(n,0,-1):
    if i+lst[i][0]>n+1:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(lst[i][1]+dp[i+lst[i][0]], dp[i+1])
print(dp[1])