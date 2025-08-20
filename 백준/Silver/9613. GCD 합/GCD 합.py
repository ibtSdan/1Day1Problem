test = int(input())

def gcd(a, b):
    if b==0:
        return a
    return gcd(b,a%b)

for _ in range(test):
    lst = list(map(int,input().split()))
    ans = 0
    for i in range(1, len(lst)-1):
        for j in range(i+1,len(lst)):
            ans += gcd(lst[i],lst[j])
    print(ans)