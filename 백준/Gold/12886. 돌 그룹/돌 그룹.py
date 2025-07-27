from collections import deque
import sys

stone = list(map(int, input().split()))
visited = set()
stone.sort()
dq = deque()

def BFS():
    a, b, c = stone
    visited.add((a,b,c))
    dq.append((a,b,c))
    while dq:
        x, y, z = dq.popleft()
        if x==y==z:
            print(1)
            sys.exit()
            
        lst = [x,y,z]
        for i, j in [(0,1), (0,2), (1,2)]:
            if lst[i]!=lst[j]:
                newlst = [x,y,z]
                newlst[j] = newlst[j]-newlst[i]
                newlst[i] = newlst[i]+newlst[i]
                newlst = tuple(sorted(newlst))
                if newlst not in visited:
                    dq.append(newlst)
                    visited.add(newlst)
BFS()
print(0)