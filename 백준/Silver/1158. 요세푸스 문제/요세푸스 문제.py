from collections import deque

n, k = map(int, input().split())
dq = deque([i for i in range(1,n+1)])
ans = []
while len(dq)>1:
    for _ in range(k-1):
        dq.append(dq.popleft())
    ans.append(dq.popleft())
ans.append(dq[0])

print(f"<{', '.join(map(str,ans))}>")