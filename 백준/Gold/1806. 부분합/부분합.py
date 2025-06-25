import sys
input = sys.stdin.readline

n, m = map(int,input().split())
lst = list(map(int,input().split()))

s = 0
e = 0
ans = float('inf')
nSum = 0

while True:
    if nSum >= m:
        ans = min(ans, e-s)
        nSum -= lst[s]
        s += 1
    elif e==n:
        break
    else:
        nSum += lst[e]
        e += 1

if ans == float('inf'):
    print(0)
else:
    print(ans)