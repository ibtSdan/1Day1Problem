def solution(k, tangerine):
    ans = 0
    count = [0] * 10000001
    for i in tangerine:
        count[i] += 1
    count.sort(reverse=True)
    
    for i in count:
        if i:
            ans += 1
            if i>=k:
                return ans
            else:
                k -= i