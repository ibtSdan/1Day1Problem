def solution(s):
    s = list(s)
    upper = []
    for i in s:
        if i.isupper():
            upper.append(i)
    s.sort(reverse=True)
    upper.sort(reverse=True)
    
    return ''.join(i for i in s if not i.isupper()) + ''.join(i for i in upper)