import sys, heapq
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())
hq = []
parent = [0] * (n+1)
for i in range(1,n+1):
    parent[i] = i
    
for _ in range(m):
    s, e, w = map(int, input().split())
    heapq.heappush(hq, (w,s,e))
        
def find(a):
    if parent[a] == a:
        return a
    else:
        parent[a] = find(parent[a])
        return parent[a]
        
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a
        
useEdge = 0
result = 0
            
while useEdge < n-1:
    w, s, e = heapq.heappop(hq)
    if find(s) != find(e):
        union(s, e)
        useEdge += 1
        result += w
        
print(result)