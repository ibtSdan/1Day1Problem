def solution(n, lost, reserve):
    re = [i for i in reserve if i not in lost]
    lo = [i for i in lost if i not in reserve]
    lst = [0] + [1 if i not in lo else 0 for i in range(1, n+1)]
    
    lo.sort()
    for i in lo:
        if i-1 in re:
            lst[i] = 1
            re.remove(i-1)
        elif i+1 in re:
            lst[i] = 1
            re.remove(i+1)
    return lst.count(1)