n, k = map(int,input().split())
A = [0]*n
for i in range(n):
    A[i] = int(input())

cnt = 0

for i in range(n-1,-1,-1):
    if A[i] <= k:
        cnt = cnt + k//A[i]
        k = k%A[i]
    if k==0:
        flag = True
        break
print(cnt)        