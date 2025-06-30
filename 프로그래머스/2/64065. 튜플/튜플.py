def solution(s):
    s = s[1:-1]
    lst = []
    idx = 0
    check = True
    while idx<len(s):
        if s[idx]=='{':
            a = []
            n = ''
        elif s[idx]=='}':
            if n:
                a.append(int(n))
            lst.append(a)
            check = True
        elif s[idx].isdigit():
            check = False
            n += s[idx]
        elif not check and s[idx]==',':
            check = True
            a.append(int(n))
            n = ''
        idx += 1

    lst.sort(key=lambda x: len(x))

    ans = []
    for i in lst:
        for j in i:
            if j not in ans:
                ans.append(j)
                break
    return ans