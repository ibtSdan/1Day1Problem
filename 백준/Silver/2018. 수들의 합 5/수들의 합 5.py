n = int(input())
s = 1
e = 1
ssum = 1
cnt = 1
while e < n:
    if ssum == n:
        cnt += 1
        e += 1
        ssum += e
    elif ssum > n:
        ssum -= s
        s += 1
    else:
        e += 1
        ssum += e
print(cnt)