import math
a,b = map(int,input().split())

A = [0] * (int(math.sqrt(b))+1)
for i in range(2,len(A)):
    A[i] = i
    
# 소수 구하기
for i in range(2,int(math.sqrt(b))+1):
    if A[i]==0:
        continue
    for j in range(i+i, int(math.sqrt(b))+1, i):
        A[j] = 0
        
cnt = 0
for i in range(2,int(math.sqrt(b))+1):
    if A[i]==0:
        continue
    n = i*i
    while n<=b:
        if n >= a:
            cnt += 1
        n = n*i
print(cnt)