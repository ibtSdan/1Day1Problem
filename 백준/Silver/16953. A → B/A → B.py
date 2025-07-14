import sys
from collections import deque

a, b = map(int, input().split())
visited = set()
dq = deque()
dq.append((a,1))
visited.add(a)

while dq:
    now, cnt = dq.popleft()
    if now==b:
        print(cnt)
        sys.exit()
    
    for i in [now*2, int(str(now)+"1")]:
        if i<=b and i not in visited:
            dq.append((i, cnt+1))

print(-1)