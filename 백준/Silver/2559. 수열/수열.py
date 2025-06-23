import sys
input = sys.stdin.readline
n, k = map(int,input().split())
days = list(map(int,input().split()))

s = 0
e = k-1
total = sum(days[i] for i in range(k))
ans = total

while e<n-1:
    e += 1
    total += days[e]
    total -= days[s]
    s += 1
    if total > ans:
        ans = total
print(ans)