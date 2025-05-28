from collections import deque

n, k = map(int, input().split())
lst = list(i for i in range(1, n+1))
dq = deque(lst)
ans = []

while dq:
    for _ in range(k-1):
        dq.append(dq.popleft())
    ans.append(dq.popleft())

print('<', end='')
for i in range(len(ans)-1):
    print(ans[i], end=', ')
print(str(ans[-1])+'>')