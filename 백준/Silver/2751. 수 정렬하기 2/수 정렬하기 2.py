import sys
input = sys.stdin.readline
n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
A.sort()
for i in range(n):
    print(A[i])