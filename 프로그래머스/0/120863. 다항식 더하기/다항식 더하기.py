def solution(p):
    p = p.replace(' ', '')
    lst = list(p.split("+"))
    x = []
    n = []
    for i in lst:
        if 'x' in i:
            x.append(1 if i=='x' else int(i[:-1]))
        else:
            n.append(int(i))
    s_sum = '' if x==[1] else str(sum(x))
    n_sum = str(sum(n))
    
    if n and x:
        return s_sum+'x'+' + '+n_sum
    elif x and not n:
        return s_sum+'x'
    else:
        return n_sum