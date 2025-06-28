from collections import deque
import sys

n = int(input())
if n==1:
    print(1)
    sys.exit()
    
dq = deque([i for i in range(2,n+1)])

while len(dq)>1:
    dq.append(dq.popleft())
    dq.popleft()
print(dq[0])