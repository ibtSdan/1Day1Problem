import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()
for _ in range(n):
    qus = input().strip()
    if len(qus.split())==2:
        q, x = qus.split()
        dq.append(x)
    elif qus=='pop':
        print(dq.popleft() if dq else -1)
    elif qus=='size':
        print(len(dq))
    elif qus=='empty':
        print(1 if not dq else 0)
    elif qus=='front':
        print(dq[0] if dq else -1)
    elif qus=='back':
        print(dq[-1] if dq else -1)