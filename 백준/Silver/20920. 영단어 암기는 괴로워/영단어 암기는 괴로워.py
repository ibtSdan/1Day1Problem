import sys
from collections import Counter
input = sys.stdin.readline

n, m = map(int,input().split())
A = []
for _ in range(n):
    word = input().strip()
    if len(word)>=m:
        A.append(word)

count = Counter(A)
lst = sorted(count.keys(), key=lambda x: (-count[x], -len(x), x))

for i in lst:
    print(i)