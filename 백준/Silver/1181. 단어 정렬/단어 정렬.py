import sys
input = sys.stdin.readline

n = int(input())
s_set = set()
for _ in range(n):
    s_set.add(input().strip())
lst = [[] for _ in range(51)]
for s in s_set:
    lst[len(s)].append(s)
for i in range(51):
    lst[i].sort()
for i in range(51):
    if lst[i]:
        for j in lst[i]:
            print(j)