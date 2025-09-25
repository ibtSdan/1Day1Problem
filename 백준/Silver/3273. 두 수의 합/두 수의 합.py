n = int(input())
lst = list(map(int,input().split()))
lst.sort()
k = int(input())

ans = 0
s = 0
e = n-1
while s<e:
    if lst[s]+lst[e]==k:
        ans += 1
        s += 1
        e -= 1
    elif lst[s]+lst[e]<k:
        s += 1
    else:
        e -= 1
print(ans)