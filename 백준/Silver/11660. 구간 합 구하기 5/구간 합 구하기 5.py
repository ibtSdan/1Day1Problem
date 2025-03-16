import sys
input = sys.stdin.readline
n, m = map(int, input().split())

a = [[0]*(n+1)]
D = [[0]*(n+1) for _ in range(n+1)]

for _ in range(n):
    a_row = [0] + [int(i) for i in input().split()]
    a.append(a_row)

for i in range(1,n+1):
    for j in range(1,n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + a[i][j]
        
for _ in range(m):
    x1,y1,x2,y2 = map(int, input().split())
    print(D[x2][y2]-D[x2][y1-1]-D[x1-1][y2]+D[x1-1][y1-1])