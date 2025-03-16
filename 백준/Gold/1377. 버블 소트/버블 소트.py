import sys
input = sys.stdin.readline
n = int(input())
A = []
for i in range(n):
    num = int(input())
    A.append((num,i))

# 정렬
M = 0
A.sort()
for i in range(n):
    if A[i][1]-i > M:
        M = A[i][1]-i
print(M+1)