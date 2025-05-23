import sys
input = sys.stdin.readline

n = int(input())
d = [0]*(n+2)
t = []
p = []
for _ in range(n):
    tt, pp = map(int, input().split())
    t.append(tt)
    p.append(pp)

for i in range(n-1, -1, -1):
    if i+t[i] > n:
        d[i] = d[i+1]
    else:
        d[i] = max(d[i+1], d[i+t[i]]+p[i])
print(d[0])