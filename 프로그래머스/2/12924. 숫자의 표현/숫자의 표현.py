def solution(n):
    cnt = 0
    s = 1
    e = 2
    ssum = s+e
    if n==1:
        return 1
    elif n==2:
        return 1
    
    while e<=n:
        if ssum==n:
            cnt += 1
            e += 1
            ssum += e
        elif ssum>n:
            ssum -= s
            s += 1
        else:
            e += 1
            ssum += e
    return cnt