def solution(brown, yellow):
    area = brown + yellow
    lst = divisors(area)
    for garo, sero in lst:
        if 2*(garo+sero-2) == brown and (garo-2)*(sero-2) == yellow:
            return [garo, sero]
    
    
def divisors(n):
    s = set()
    for i in range(3, int(n**0.5)+1):
        if n%i==0:
            s.add((n//i, i))
    return list(s)