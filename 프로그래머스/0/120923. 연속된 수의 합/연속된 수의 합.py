def solution(num, total):
    result = 0
    s, e = total-num+1, total
    n = sum(i for i in range(s,e+1))
    while n != total:
        if n > total:
            e -= 1
            s -= 1
        else:
            s += 1
            e += 1
        n = sum(i for i in range(s,e+1))
    
    return [i for i in range(s,e+1)]