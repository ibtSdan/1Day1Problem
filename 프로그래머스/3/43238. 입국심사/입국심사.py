def solution(n, times):
    s = 0
    e = n*max(times)
    ans = e
    while s<=e:
        mid = (s+e)//2
        total = sum(mid//times[i] for i in range(len(times)))
        
        if total>=n:
            ans = min(ans, mid)
            e = mid - 1
        else:
            s = mid + 1
    return ans