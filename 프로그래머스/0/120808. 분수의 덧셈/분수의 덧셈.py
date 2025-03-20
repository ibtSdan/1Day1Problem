def solution(numer1, denom1, numer2, denom2):
    n = lcd(denom1, denom2)
    numer1 = numer1*(n//denom1) if denom1 != n else numer1
    numer2 = numer2*(n//denom2) if denom2 != n else numer2

    g = gcd(numer1+numer2,n)

    return [(numer1+numer2)//g, n//g]
    
    
    
def gcd(a,b):
    if b==0:
        return a
    return gcd(b,a%b)

def lcd(a,b):
    return (a*b)//gcd(a,b)