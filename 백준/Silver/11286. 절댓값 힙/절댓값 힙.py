import heapq, sys
input = sys.stdin.readline
n = int(input())
pq = []

for _ in range(n):
    num = int(input())
    if num != 0:
        heapq.heappush(pq, (abs(num), num))
    else:
        if pq:
            print(heapq.heappop(pq)[1])
        else:
            print(0)