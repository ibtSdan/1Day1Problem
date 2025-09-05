from collections import deque
import sys
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    a, b = map(int, input().split())
    dq = deque()
    visited = [False] * (10000)
    dq.append((a,''))
    visited[a] = True
    while dq:
        now, ans = dq.popleft()
        if now==b:
            print(ans)
            break
        while len(str(now))<4:
            now = '0'+str(now)
        new = int(now)*2%10000
        if not visited[new]:
            dq.append((new, ans+'D'))
            visited[new] = True
        new = 9999 if int(now)==0 else int(now)-1
        if not visited[new]:
            dq.append((new,ans+'S'))
            visited[new] = True
        new = int(str(now)[3]+str(now)[:3])
        if not visited[new]:
            dq.append((new,ans+'R'))
            visited[new] = True
        new = int(str(now)[1:]+str(now)[0])
        if not visited[new]:
            dq.append((new,ans+'L'))
            visited[new] = True