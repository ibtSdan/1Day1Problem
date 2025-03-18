def solution(n):
    cnt = 0
    for i in range(4,n+1):
        if division(i):
            cnt += 1
    return cnt

def division(a):
    s = set()
    cnt = 0
    for i in range(1,int(a**0.5)+1):
        if a%i==0:
            s.add(i)
            s.add(a//i)
        if len(s)>=3:
            return True
        
    return False