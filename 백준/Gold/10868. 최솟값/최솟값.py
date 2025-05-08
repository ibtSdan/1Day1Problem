import sys
input = sys.stdin.readline

n, m = map(int, input().split())
power = 1
while 2**power <= n:
    power += 1
index = 2**power
A = [sys.maxsize] * (index*2)
for i in range(index, index+n):
    A[i] = int(input())
        
for i in range(index-1, 0, -1):
    A[i] = min(A[i*2], A[i*2+1])
        
def getMin(s, e):
    minVal = A[s]
    while s <= e:
        if s%2==1:
            minVal = min(minVal, A[s])
        if e%2==0:
            minVal = min(minVal, A[e])
        s = (s+1)//2
        e = (e-1)//2
    return minVal
                
for _ in range(m):
    s, e = map(int, input().split())
    print(getMin(s+index-1, e+index-1))