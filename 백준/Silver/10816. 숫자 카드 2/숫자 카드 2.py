import sys
input = sys.stdin.readline

n = int(input())
lst = list(map(int,input().split()))
m = int(input())
find = list(map(int,input().split()))
A = [0] * (20000001)

for i in lst:
    A[i+10000000] += 1
    
for i in find:
    print(A[i+10000000])