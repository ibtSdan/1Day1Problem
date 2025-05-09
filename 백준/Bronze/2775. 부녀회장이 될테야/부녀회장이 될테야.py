import sys
input = sys.stdin.readline

D = [[0 for _ in range(15)] for _ in range(15)]
for i in range(1, 15):
    D[0][i] = i
    D[i][1] = 1
        
for i in range(1, 15):
    for j in range(2, 15):
        D[i][j] = D[i][j-1] + D[i-1][j]
        
m = int(input())
for _ in range(m):
    n = int(input())
    k = int(input())
    print(D[n][k])