import sys
n = int(input())
A = list(map(int, sys.stdin.readline().split()))
stack = []
NGE = [-1]*n

for i in range(n):
    while stack and A[stack[-1]]<A[i]:
        NGE[stack.pop()] = A[i]
    stack.append(i)

for i in NGE:
    print(i, end = ' ')