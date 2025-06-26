import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dis = [0] * 1000001
for _ in range(n):
    ice, x = map(int,input().split())
    dis[x] = ice
l = k*2
ans = sum(dis[:l])
total = ans

for i in range(l,1000001):
    total = total + dis[i] - dis[i-l-1]
    ans = max(total,ans)
    
print(ans)