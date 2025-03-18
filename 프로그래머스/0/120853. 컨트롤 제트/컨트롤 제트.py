def solution(s):
    s = list(s.split())
    result = 0
    for i in range(len(s)):
        if s[i]=='Z':
            result -= int(s[i-1])
            continue
        result += int(s[i])
    return result