import sys
input = sys.stdin.readline
        
def gcd(a,b):
    if a%b==0:
        return b
    return gcd(b,a%b)

n = int(input())
for _ in range(n):
    a,b = map(int, input().split())
    ans = gcd(a,b)
    print(a*b//ans)