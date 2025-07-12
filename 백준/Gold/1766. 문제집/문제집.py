import heapq

n, m = map(int, input().split())
D = [0]*(n+1)
A = [[] for _ in range(n+1)]
for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    D[e] += 1

q = []
for i in range(1, n+1):
    if D[i]==0:
        heapq.heappush(q, i)
        
while q:
    now = heapq.heappop(q)
    print(now, end=' ')
    for i in A[now]:
        D[i] -= 1
        if D[i]==0:
            heapq.heappush(q, i)