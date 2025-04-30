import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
start = int(input())
A = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, w = map(int, input().split())
    A[u].append((v,w))
    
distance = [int(1e9)] * (n+1)
hq = []
heapq.heappush(hq, (0, start))
distance[start] = 0

while hq:
    dis, now = heapq.heappop(hq)
    if dis > distance[now]:
        continue
    for vv, ww in A[now]:
        cost = ww + dis
        if cost < distance[vv]:
            distance[vv] = cost
            heapq.heappush(hq, (cost, vv))

for i in range(1,n+1):
    if distance[i] == int(1e9):
        print("INF")
    else:
        print(distance[i])