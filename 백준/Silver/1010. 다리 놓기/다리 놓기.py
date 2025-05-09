import sys
input = sys.stdin.readline

k = int(input())
D = [[0 for _ in range(30)] for _ in range(30)]
for i in range(30):
    D[i][0] = 1
    D[i][i] = 1
    D[i][1] = i
    
for i in range(1, 30):
    for j in range(1, i):
        D[i][j] = D[i-1][j] + D[i-1][j-1]
        
for _ in range(k):
    n, m = map(int, input().split())
    print(D[m][n])