n = int(input())
count = 1
s = 1
e = 1
ssum = 1
while e < n:
    if ssum == n:
        count += 1
        e += 1
        ssum += e
    elif ssum > n:
        ssum -= s
        s += 1
    else:
        e += 1
        ssum += e
print(count)