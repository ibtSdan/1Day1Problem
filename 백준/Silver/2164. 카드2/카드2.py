from collections import deque

n = int(input())
lst = [i for i in range(1,n+1)]
dq = deque(lst)
while len(dq)>1:
    dq.popleft()
    dq.append(dq.popleft())
print(dq[0])