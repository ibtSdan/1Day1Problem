import sys, heapq
input = sys.stdin.readline
n = int(input())
answer = 0
pos = []
neg = []

for _ in range(n):
    num = int(input())
    if num>0:
        heapq.heappush(pos, -num)
    else:
        heapq.heappush(neg, num)
        
while len(pos) > 1:
    f = -heapq.heappop(pos)
    s = -heapq.heappop(pos)
    if f*s >= f+s:
        answer += f*s
    else:
        answer += f+s
while len(neg) > 1:
    f = heapq.heappop(neg)
    s = heapq.heappop(neg)
    if f*s >= f+s:
        answer += f*s
    else:
        answer += f+s
if pos:
    answer += -heapq.heappop(pos)
if neg:
    answer += heapq.heappop(neg)

print(answer)