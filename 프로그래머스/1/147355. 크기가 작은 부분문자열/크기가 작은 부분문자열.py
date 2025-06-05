def solution(t, p):
    ans = 0
    for i in range(len(t)-len(p)+1):
        s = t[i:i+len(p)]
        if int(s)<=int(p):
            ans += 1
    return ans