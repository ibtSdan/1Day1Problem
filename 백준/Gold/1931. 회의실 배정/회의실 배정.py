import heapq, sys
input = sys.stdin.readline
n = int(input())
A = []
answer = 1
for _ in range(n):
    s, e = map(int,input().split())
    heapq.heappush(A, (e,s))
    
f_e, f_s = heapq.heappop(A)
while A:
    s_e, s_s = heapq.heappop(A)
    if f_e <= s_s:
        answer += 1
        f_s, f_e = s_s, s_e
print(answer)