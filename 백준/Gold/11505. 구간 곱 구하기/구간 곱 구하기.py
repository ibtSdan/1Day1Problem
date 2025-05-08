import sys
input = sys.stdin.readline
MOD = 1000000007

n, m, k = map(int, input().split())
power = 1
while 2**power < n:
    power += 1
index = 2**power
tree = [1] * (index*2)
for i in range(index, index+n):
    tree[i] = int(input())
        
for i in range(index-1, 0, -1):
    tree[i] = tree[i*2] * tree[i*2+1] % MOD
    
def update(idx, val):
    tree[idx] = val
    while idx>0:
        idx //= 2
        tree[idx] = tree[idx*2] * tree[idx*2+1] % MOD
        
def getMul(s, e):
    mul = 1
    while s<=e:
        if s%2==1:
            mul *= tree[s] % MOD
        if e%2==0:
            mul *= tree[e] % MOD
        s = (s+1)//2
        e = (e-1)//2
    return mul
    
for _ in range(m+k):
    type, s, e = map(int, input().split())
    if type == 1:
        update(s+index-1, e)
    elif type == 2:
        print(getMul(s+index-1, e+index-1)%MOD)