def solution(n, m):
    ans = []
    ans.append(gcd(n,m))
    ans.append(n*m//gcd(n,m))
    return ans

def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)