def solution(n):
    c = 0
    for i in range(1,int(n**0.5)+1):
        if n%i==0:
            c += 1
    c *= 2
    if int(n**0.5)==n**0.5:
        c -= 1
    return c