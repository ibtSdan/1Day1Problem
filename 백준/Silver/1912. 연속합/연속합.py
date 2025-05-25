n = int(input())
lst = list(map(int, input().split()))

d = [0]*n
d[0] = lst[0]
ans = lst[0]

for i in range(1,n):
    d[i] = max(d[i-1]+lst[i], lst[i])
    ans = max(ans, d[i])
    
print(ans)