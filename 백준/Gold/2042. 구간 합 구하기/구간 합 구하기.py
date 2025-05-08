import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
power = 1
while 2**power < n:
    power += 1
index = 2**power
A = [0]*(index*2)

for i in range(index, index+n):
    A[i] = int(input())

for i in range(index-1, -1, -1):
    A[i] = A[i*2] + A[i*2+1]
    
def getSum(s, e):
    summ = 0
    while s<=e:
        if s%2==1:
            summ += A[s]
        if e%2==0:
            summ += A[e]
        s = (s+1)//2
        e = (e-1)//2
    return summ
    
def update(idx, val):
    diff = val - A[idx]
    while idx>0:
        A[idx] += diff
        idx //= 2
        
for _ in range(m+k):
    type, s, e = map(int, input().split())
    if type == 1:
        update(s+index-1, e)
    if type == 2:
        print(getSum(s+index-1, e+index-1))