def solution(s):
    a = []
    for i in range(len(s)):
        a.append(s[i])
        while len(a)>=2 and a[-1] == a[-2]:
            a.pop()
            a.pop()
    return 1 if not a else 0
            