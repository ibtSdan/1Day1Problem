from collections import Counter
import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
m = int(input())
find = list(map(int, input().split()))

cnt = Counter(lst)
for i in find:
    print(cnt[i], end=' ')