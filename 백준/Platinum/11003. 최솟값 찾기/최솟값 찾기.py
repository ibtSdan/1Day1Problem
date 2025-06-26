from collections import deque

n, l = map(int,input().split())
lst = list(map(int,input().split()))
dq = deque()

for i in range(n):
    if dq and i - dq[0][1] >= l:
        dq.popleft()
    while dq and dq[-1][0]>=lst[i]:
        dq.pop()
    dq.append((lst[i],i))
    print(dq[0][0], end=' ')