n = int(input())
lst = []
lst.append((0,0))
for _ in range(n):
    time, pay = map(int, input().split())
    lst.append((time, pay))

dp = [0]*(n+2)
for day in range(n,0,-1):
    if day+lst[day][0]<=n+1:
        dp[day] = max(dp[day+1], lst[day][1] + dp[day+lst[day][0]])
    else:
        dp[day] = dp[day+1] 
print(max(dp))