def solution(n):
    # n, 6의 최소공배수 찾기
    # 그 값을 6으로 나누기
    n_min = (n * 6) // gcd(n, 6)
    
    return n_min // 6

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)