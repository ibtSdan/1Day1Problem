n, m = map(int, input().split())

def gcd(a, b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
    
ans = gcd(n,m)
print(''.join('1' for _ in range(ans)))