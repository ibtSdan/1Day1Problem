import sys
input = sys.stdin.readline

n, k = map(int,input().split())
lst = list(map(int,input().split()))
s = 0
e = max(lst)
result = 0

while s <= e:
    h = (s+e)//2
    total = 0
    for i in lst:
        if i>h:
            total += i-h
    if total>=k:
        result = h
        s = h+1
    else:
        e = h-1
print(result)