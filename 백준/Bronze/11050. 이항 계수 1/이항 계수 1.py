n, k = map(int, input().split())
D = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(n+1):
    D[i][i] = 1
    D[i][0] = 1
    D[i][1] = i
    
for i in range(1, n+1):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]
        
print(D[n][k])