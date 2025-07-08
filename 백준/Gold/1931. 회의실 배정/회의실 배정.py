import sys
input = sys.stdin.readline

n = int(input())
A = []
for _ in range(n):
    s, e = map(int, input().split())
    A.append((s,e))
A.sort(key=lambda x: (x[1],x[0]))

cnt = 0
end = 0
for s, e in A:
    if s >= end:
        cnt += 1
        end = e
print(cnt)