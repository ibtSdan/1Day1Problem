n = int(input())
dis = list(map(int, input().split()))
exp = list(map(int, input().split()))
ans = 0
idx = 0
check = idx
while idx<n-1:
    if exp[check]>=exp[idx+1]:
        ans += exp[check]*sum(dis[check:idx+1])
        check = idx+1
    idx += 1
        
print(ans)