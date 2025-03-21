n = int(input())
lst = list(map(int, input().split()))
lst.sort()
cnt = 0
for i in range(n):
    k = lst[i]
    s = 0
    e = n-1
    while s < e:
        if lst[s]+lst[e] == k:
            if s == i:
                s += 1
            elif e == i:
                e -= 1
            else:
                cnt +=1
                break
        elif lst[s]+lst[e] > k:
            e -= 1
        else:
            s += 1
print(cnt)