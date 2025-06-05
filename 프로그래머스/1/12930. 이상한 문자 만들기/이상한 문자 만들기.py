def solution(s):
    s = s.lower()
    ans = ''
    idx = 0
    for i in range(len(s)):
        if s[i]==' ':
            ans += s[i]
            idx = 0
        elif idx%2==0:
            ans += s[i].upper()
            idx += 1
        else:
            ans += s[i]
            idx += 1
    return ans