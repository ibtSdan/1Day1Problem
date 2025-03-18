def solution(n):
    i = 1
    while True:
        if f(i) <= n:
            i += 1
        else:
            return i-1

def f(n):
    if n==1:
        return 1
    return n * f(n-1)