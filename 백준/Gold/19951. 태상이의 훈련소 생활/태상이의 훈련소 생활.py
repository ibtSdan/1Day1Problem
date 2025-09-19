n, m = map(int,input().split())
soil = [0] + list(map(int,input().split()))
diff = [0]*(n+1)
for i in range(m):
    a,b,k = map(int,input().split())
    diff[a] += k
    if b+1<=n:
        diff[b+1] -= k
total = [0]*(n+1)
for i in range(1,n+1):
    total[i] = diff[i] + total[i-1]

for i in range(1,n+1):
    print(soil[i]+total[i],end=' ')