import math, sys
n = int(input())
A = [0] * 10000001
for i in range(2,10000001):
    A[i] = i
for i in range(2,int(math.sqrt(10000000))+1):
    if A[i]==0:
        continue
    for j in range(i+i,10000001,i):
        A[j] = 0
lst = [i for i in range(10000001) if A[i] and i>=n]

for i in lst:
    if str(i)==str(i)[::-1]:
        print(int(i))
        break