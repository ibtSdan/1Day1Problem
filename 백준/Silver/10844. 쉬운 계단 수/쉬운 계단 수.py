n = int(input())
d = [[0 for j in range(10)] for i in range(n+1)]
MOD = 1000000000

for i in range(1,10):
    d[1][i] = 1

for i in range(2,n+1):
    for j in range(10):
        if j==0:
            d[i][j] = d[i-1][1]
        elif j==9:
            d[i][j] = d[i-1][8]
        else:
            d[i][j] = (d[i-1][j-1] + d[i-1][j+1]) % MOD
            
cnt = 0
for i in range(10):
    cnt += d[n][i]
    
print(cnt % MOD)