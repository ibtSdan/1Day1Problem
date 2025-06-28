from collections import deque
n, k = map(int,input().split())
dq = deque([i for i in range(1,n+1)])
ans = []

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    ans.append(dq.popleft())

answer = ', '.join(str(i) for i in ans)
print("<"+answer+">")