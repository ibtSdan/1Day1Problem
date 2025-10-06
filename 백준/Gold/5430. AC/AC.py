from collections import deque

test = int(input())
for _ in range(test):
    control = list(input().strip())
    n = int(input())
    string = input().strip()
    if string=='[]':
        dq = deque()
    else:
        dq = deque(string[1:-1].split(','))
    error = False
    re = False
    for c in control:
        if c=='R':
            re = not re
        elif c=='D':
            if not dq:
                error = True
                break
            if re:
                dq.pop()
            else:
                dq.popleft()
    if error:
        print('error')
    else:
        if re:
            dq.reverse()
        print('['+','.join(dq)+']')