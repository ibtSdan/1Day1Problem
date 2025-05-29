from collections import deque

n, k = map(int, input().split())

def bfs(n, k):
    MAX = 100001
    visited = [False]*MAX
    dq = deque()
    dq.append((n,0))
    visited[n] = True
    while dq:
        current, time = dq.popleft()
        if current == k:
            return time
        for next_n in (current-1, current+1, current*2):
            if 0<=next_n<MAX and not visited[next_n]:
                visited[next_n] = True
                dq.append((next_n, time+1))
                
print(bfs(n,k))