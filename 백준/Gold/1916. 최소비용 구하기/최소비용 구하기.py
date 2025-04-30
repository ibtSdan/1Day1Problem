import sys, heapq
input = sys.stdin.readline
INF = int(1e9)
    
n = int(input())
m = int(input())
A = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    A[u].append((v,w))
start, arrive = map(int, input().split())
total = [INF] * (n+1)
total[start] = 0
hq = []
heapq.heappush(hq, (0, start))

while hq:
    distance, node = heapq.heappop(hq)
    if distance > total[node]:
        continue
    for next, weight in A[node]:
        cost = weight + total[node]
        if cost < total[next]:
            total[next] = cost
            heapq.heappush(hq, (cost, next))
            
print(total[arrive])