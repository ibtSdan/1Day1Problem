from collections import deque

n, k = map(int, input().split())
lst = [i for i in range(1,n+1)]
dq = deque(lst)
ans = []

while len(dq)>=2:
    for _ in range(k-1):
        dq.append(dq.popleft())
    ans.append(str(dq.popleft()))
ans.append(str(dq[0]))

print('<'+', '.join(ans)+'>')