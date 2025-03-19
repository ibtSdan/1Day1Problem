def solution(a, b):
    # 기약분수 -> 최대공약수 찾기
    n = gcd(a,b)
    a = a//n
    b = b//n
    
    # 분모가 2와 5 소인수
    for i in [2,5]:
        while b%i==0:
            b = b//i

    return 1 if b==1 else 2

def gcd(a,b):
    if b == 0:
        return a
    return gcd(b,a%b)