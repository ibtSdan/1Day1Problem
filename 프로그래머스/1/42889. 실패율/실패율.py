def solution(n, stages):
    fail = [0] * (n+1)
    arrive = [0] * (n+1)
    fail_rate = []
    for p in stages:
        if p>n:
            p = n
            fail[p] -= 1
        fail[p] += 1
        for i in range(1,p+1):
            arrive[i] += 1
    
    for i in range(1,n+1):
        fail_p = fail[i]
        arrive_p = arrive[i]
        if arrive_p == 0:
            fail_rate.append((0,i))
            continue
        fail_rate.append((fail_p/arrive_p, i))
    
    fail_rate.sort(key=lambda x: (-x[0], x[1]))
    
    ans = []
    for f, stage in fail_rate:
        ans.append(stage)
    return ans