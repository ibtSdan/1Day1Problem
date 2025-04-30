import sys, heapq
input = sys.stdin.readline

INF = int(1e9)
n, m = map(int, input().split())
start = int(input())
A = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    A[u].append((v,w))

total = [INF] * (n+1)
hq = []
heapq.heappush(hq, (0, start))
total[start] = 0
while hq:
    distance, next = heapq.heappop(hq)
    if distance > total[next]:
        continue
    for edge, weight in A[next]:
        cost = total[next] + weight
        if cost < total[edge]:
            total[edge] = cost
            heapq.heappush(hq, (cost, edge))

for i in range(1,n+1):
    if total[i] == INF:
        print("INF")
    else:
        print(total[i])