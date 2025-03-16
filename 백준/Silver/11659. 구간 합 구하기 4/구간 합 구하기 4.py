import sys
n, m = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
s = [0]
temp = 0
for i in lst:
    temp += i
    s.append(temp)

for _ in range(m):
    i, j = map(int, sys.stdin.readline().split())
    print(s[j]-s[i-1])

# S[j]-S[i-1] 은 i부터 j까지의 합
