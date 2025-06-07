import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
dq = deque()

for _ in range(n):
    cmd = input().split()
    if len(cmd)==2:
        num = cmd[1]
    if cmd[0] == 'push_front':
        dq.appendleft(num)
    elif cmd[0] == 'push_back':
        dq.append(num)
    elif cmd[0] == 'pop_front':
        if dq:
            print(dq.popleft())
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if dq:
            print(dq.pop())
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(dq))
    elif cmd[0] == 'empty':
        if dq:
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if dq:
            print(dq[0])
        else:
            print(-1)
    else:
        if dq:
            print(dq[-1])
        else:
            print(-1)