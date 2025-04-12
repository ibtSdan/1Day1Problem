import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

dq = deque()
for i in range(n):
    while dq and dq[-1][0] > lst[i]:
        dq.pop()
    dq.append((lst[i], i))
    if dq[-1][1] - dq[0][1] >= m:
        dq.popleft()
    print(dq[0][0], end=' ')