import math
a, b = map(int, input().split())
A = [0] * (b+1)
for i in range(2,b+1):
    A[i] = i

for i in range(2,int(math.sqrt(b))+1):
    if A[i]==0:
        continue
    for j in range(i+i, b+1, i):
        A[j] = 0
        
for i in range(a,b+1):
    if A[i]:
        print(A[i])