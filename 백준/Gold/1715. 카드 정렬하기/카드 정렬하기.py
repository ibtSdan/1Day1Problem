import sys, heapq
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    heapq.heappush(A, int(input()))

cnt = 0
while len(A)>1:
    f = heapq.heappop(A)
    s = heapq.heappop(A)
    plus = f+s
    cnt += plus
    heapq.heappush(A, plus)
    
print(cnt)