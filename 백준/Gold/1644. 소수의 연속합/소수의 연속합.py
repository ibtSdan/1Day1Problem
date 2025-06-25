import sys

n = int(input())

if n < 2:
    print(0)
    sys.exit()
    
lst = [0] * (n+1)
for i in range(2,n+1):
    lst[i] = i
    
for i in range(2,int(n**0.5)+1):
    if lst[i]==0:
        continue
    for j in range(i*2,n+1,i):
        lst[j] = 0

A = []
for i in lst:
    if i:
        A.append(i)
        
s = 0
e = 0
cnt = 0
total = 0

while True:
    if total >= n:
        if total == n:
            cnt += 1
        total -= A[s]
        s += 1
    elif e == len(A):
        break
    else:
        total += A[e]
        e += 1
print(cnt)