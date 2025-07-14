from collections import deque

def solution(x, y, n):
    visited = [False] * 1000001
    dq = deque()
    dq.append((x,0))
    visited[x] = True
    
    while dq:
        now = dq.popleft()
        if now[0]==y:
            return now[1]
        
        for i in [now[0]+n, now[0]*2, now[0]*3]:
            if i<=y and not visited[i]:
                dq.append((i, now[1]+1))
                visited[i] = True
            
    return -1