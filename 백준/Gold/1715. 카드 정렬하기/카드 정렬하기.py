import sys, heapq
n = int(input())
A = []
for _ in range(n):
    heapq.heappush(A,int(input()))
answer = 0
while len(A)>1:
    f = heapq.heappop(A)
    s = heapq.heappop(A)
    add = f + s
    answer += add
    heapq.heappush(A, add)

print(answer)