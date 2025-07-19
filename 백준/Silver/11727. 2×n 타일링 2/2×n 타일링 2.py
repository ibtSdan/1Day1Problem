n = int(input())
A = [[0, 0] for _ in range(n+1)]
A[1][0] = 1
for i in range(2, n+1):
    A[i][0] = (A[i-1][0] + A[i-1][1])%10007
    A[i][1] = (A[i-1][0]*2)%10007
print((A[n][0]+A[n][1])%10007)