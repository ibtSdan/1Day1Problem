import sys
input = sys.stdin.readline
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
x = int(input())

s = 0
e = len(lst)-1
cnt = 0

while s<e:
    if lst[s]+lst[e]==x:
        cnt += 1
        s += 1
        e -= 1
    elif lst[s]+lst[e]>x:
        e -= 1
    else:
        s += 1
print(cnt)