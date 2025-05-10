def solution(s):
    lst = list(map(int, s.split(' ')))
    mmin = min(lst)
    mmax = max(lst)
    return str(mmin) + ' ' + str(mmax)