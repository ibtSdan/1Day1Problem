import sys
from collections import deque

n, l = map(int,input().split())
lst = list(map(int, sys.stdin.readline().split()))
dq = deque()

for i in range(n):
    while dq and dq[-1][0] > lst[i]:
        dq.pop()
    dq.append((lst[i],i))
    if dq[-1][1]-dq[0][1] >= l:
        dq.popleft()
    print(dq[0][0], end = ' ')