from collections import deque

f, s, g, u, d = map(int, input().split())
dq = deque()
visited = [False]*(f+1)
dq.append((s,0))
visited[s] = True
check = False
while dq:
    now, time = dq.popleft()
    if now==g:
        print(time)
        check = True
        break
    for i in [now+u, now-d]:
        if 1<=i<=f and not visited[i]:
            dq.append((i,time+1))
            visited[i] = True
if not check:
    print("use the stairs")