n = int(input())
A = list(map(int, input().split()))
A.sort()
S = [0] * n
S[0] = A[0]

for i in range(1,n):
    S[i] = S[i-1] + A[i]
    
print(sum(S))