import sys
from collections import deque
input = sys.stdin.readline

test = int(input())
for _ in range(test):
    n, f_idx = map(int, input().split())
    lst = list(map(int, input().split()))
    dq = deque()
    cnt = 0
    for i in range(len(lst)):
        dq.append((lst[i], i))
    while dq:
        now, idx = dq.popleft()
        if any(now<x[0] for x in dq):
            dq.append((now, idx))
        else:
            cnt += 1
            if idx==f_idx:
                print(cnt)
                break