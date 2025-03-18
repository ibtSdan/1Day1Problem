def solution(s):
    result = []
    ss = set(s)
    for i in ss:
        if s.count(i)==1:
            result.append(i)
    result.sort()
    return ''.join(result)