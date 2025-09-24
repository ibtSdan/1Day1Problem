n = int(input())
lst = list(map(int, input().split()))
lst.sort()

m = int(input())
find = list(map(int, input().split()))

for k in find:
    s = 0
    e = n-1
    check = False
    while s<=e:
        mid = (s+e)//2
        if lst[mid]==k:
            print(1)
            check = True
            break
        elif lst[mid]>k:
            e = mid-1
        else:
            s = mid+1
    if not check:
        print(0)