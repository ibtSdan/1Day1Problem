import sys
n = int(input())
lst = list(map(int, input().split()))
lst.sort()
m = int(input())
find = list(map(int, input().split()))

for i in find:
    s = 0
    e = n-1
    check = False
    while s<=e:
        mid = (s+e)//2
        if lst[mid]==i:
            check = True
            break
        elif lst[mid]<i:
            s = mid+1
        else:
            e = mid-1
    if check:
        print(1, end=' ')
    else:
        print(0, end=' ')