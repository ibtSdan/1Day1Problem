import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
D = [0] * (n+1)
for _ in range(m):
    u, v = map(int, input().split())
    A[u].append(v)
    D[v] += 1

dq = deque()
for i in range(1,n+1):
    if D[i] == 0:
        dq.append(i)
            
while dq:
    now = dq.popleft()
    print(now, end=' ')
    for i in A[now]:
        D[i] -= 1
        if D[i] == 0:
            dq.append(i)